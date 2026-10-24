
from flask import Flask, jsonify, request

from jwt_manager import JWTManager
from user_repository import user_repository

from datetime import date
from decimal import Decimal, InvalidOperation

from auth import require_auth
from product_manager import product_manager
from purchase_manager import purchase_manager

from sqlalchemy import select
from database import SessionLocal
from models import Invoice, InvoiceItem, Product

ACCESS_TOKEN_EXPIRATION = 60 * 15
REFRESH_TOKEN_EXPIRATION = 60 * 60 * 24 * 7

app = Flask("fruit-store")

jwt_manager = JWTManager(
    access_expiration=ACCESS_TOKEN_EXPIRATION,
    refresh_expiration=REFRESH_TOKEN_EXPIRATION,
)


def get_json_data():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return None
    return data


def get_current_user(expected_type="access"):
    authorization = request.headers.get("Authorization", "")

    if not authorization.startswith("Bearer "):
        return None

    token = authorization.removeprefix("Bearer ").strip()
    decoded = jwt_manager.decode_token(token, expected_type)

    if decoded is None:
        return None

    return user_repository.get_by_id(decoded["id"])


@app.route("/liveness", methods=["GET"])
def liveness():
    return jsonify(message="Service is running"), 200


@app.route("/register", methods=["POST"])
def register():
    data = get_json_data()

    if data is None:
        return jsonify(error="A JSON body is required"), 400

    username = data.get("username")
    password = data.get("password")

    if not isinstance(username, str) or not username.strip():
        return jsonify(error="Username is required"), 400

    if not isinstance(password, str) or not password:
        return jsonify(error="Password is required"), 400

    new_user = user_repository.create(username.strip(), password)

    if new_user is None:
        return jsonify(error="Username already exists"), 409

    access_token, refresh_token = jwt_manager.generate_tokens(
        new_user["id"], new_user["role"]
    )

    return jsonify(
        access_token=access_token,
        refresh_token=refresh_token,
    ), 201


@app.route("/login", methods=["POST"])
def login():
    data = get_json_data()

    if data is None:
        return jsonify(error="A JSON body is required"), 400

    username = data.get("username")
    password = data.get("password")

    if not isinstance(username, str) or not isinstance(password, str):
        return jsonify(error="Username and password are required"), 400

    user = user_repository.get_by_credentials(username, password)

    if user is None:
        return jsonify(error="Invalid username or password"), 401

    access_token, refresh_token = jwt_manager.generate_tokens(
        user["id"], user["role"]
    )

    return jsonify(
        access_token=access_token,
        refresh_token=refresh_token,
    ), 200


@app.route("/me", methods=["GET"])
def me():
    user = get_current_user()

    if user is None:
        return jsonify(error="Missing, invalid, or expired access token"), 401

    return jsonify(
        id=user["id"],
        username=user["username"],
        role=user["role"],
    ), 200


@app.route("/refresh", methods=["POST"])
def refresh():
    data = get_json_data()

    if data is None:
        return jsonify(error="A JSON body is required"), 400

    refresh_token = data.get("refresh_token")

    if not isinstance(refresh_token, str) or not refresh_token:
        return jsonify(error="Refresh token is required"), 400

    decoded = jwt_manager.decode_token(refresh_token, "refresh")

    if decoded is None:
        return jsonify(error="Invalid or expired refresh token"), 401

    user = user_repository.get_by_id(decoded["id"])

    if user is None:
        return jsonify(error="User not found"), 404

    access_token, new_refresh_token = jwt_manager.generate_tokens(
        user["id"], user["role"]
    )

    return jsonify(
        access_token=access_token,
        refresh_token=new_refresh_token,
    ), 200



@app.route("/products", methods=["POST"])
@require_auth(required_role="admin")
def create_product():
    data = get_json_data()

    if data is None:
        return jsonify(error="A JSON body is required"), 400

    name = data.get("name")
    price = data.get("price")
    entry_date = data.get("entry_date")
    quantity = data.get("quantity")

    if not isinstance(name, str) or not name.strip():
        return jsonify(error="Name is required"), 400

    try:
        parsed_price = Decimal(str(price))
        parsed_date = date.fromisoformat(entry_date)
        parsed_quantity = int(quantity)

        if not parsed_price.is_finite() or parsed_price <= 0:
            raise ValueError

        if isinstance(quantity, bool) or parsed_quantity <= 0:
            raise ValueError

    except (ValueError, TypeError, InvalidOperation):
        return jsonify(
            error="Invalid price, entry_date, or quantity"
        ), 400

    product = product_manager.create(
        name.strip(),
        parsed_price,
        parsed_date.isoformat(),
        parsed_quantity,
    )

    return jsonify(product), 201


@app.route("/products", methods=["GET"])
@require_auth(required_role="admin")
def get_products():
    return jsonify(products=product_manager.get_all()), 200


@app.route("/products/<int:product_id>", methods=["GET"])
@require_auth(required_role="admin")
def get_product(product_id):
    product = product_manager.get_by_id(product_id)

    if product is None:
        return jsonify(error="Product not found"), 404

    return jsonify(product), 200


@app.route("/products/<int:product_id>", methods=["PUT"])
@require_auth(required_role="admin")
def update_product(product_id):
    data = get_json_data()

    if data is None:
        return jsonify(error="A JSON body is required"), 400

    allowed_fields = {"name", "price", "entry_date", "quantity"}

    if not data or not set(data).issubset(allowed_fields):
        return jsonify(error="Invalid or empty product fields"), 400

    existing_product = product_manager.get_by_id(product_id)

    if existing_product is None:
        return jsonify(error="Product not found"), 404

    try:
        if "name" in data:
            if not isinstance(data["name"], str) or not data["name"].strip():
                raise ValueError
            data["name"] = data["name"].strip()

        if "price" in data:
            parsed_price = Decimal(str(data["price"]))
            if not parsed_price.is_finite() or parsed_price <= 0:
                raise ValueError
            data["price"] = str(parsed_price)

        if "entry_date" in data:
            data["entry_date"] = date.fromisoformat(
                data["entry_date"]
            ).isoformat()

        if "quantity" in data:
            if isinstance(data["quantity"], bool):
                raise ValueError
            parsed_quantity = int(data["quantity"])
            if parsed_quantity < 0:
                raise ValueError
            data["quantity"] = parsed_quantity

    except (ValueError, TypeError, InvalidOperation):
        return jsonify(error="Invalid product data"), 400

    updated_product = product_manager.update(product_id, data)

    return jsonify(updated_product), 200


@app.route("/products/<int:product_id>", methods=["DELETE"])
@require_auth(required_role="admin")
def delete_product(product_id):
    deleted = product_manager.delete(product_id)

    if not deleted:
        return jsonify(error="Product not found"), 404

    return jsonify(message="Product deleted successfully"), 200



@app.route("/purchase", methods=["POST"])
def purchase_product():
    user = get_current_user()

    if user is None:
        return jsonify(
            error="Missing, invalid, or expired access token"
        ), 401

    data = get_json_data()

    if data is None:
        return jsonify(error="A JSON body is required"), 400

    product_id = data.get("product_id")
    quantity = data.get("quantity")

    if isinstance(product_id, bool) or not isinstance(product_id, int):
        return jsonify(error="product_id must be an integer"), 400

    if isinstance(quantity, bool) or not isinstance(quantity, int):
        return jsonify(error="quantity must be an integer"), 400

    if product_id <= 0 or quantity <= 0:
        return jsonify(
            error="product_id and quantity must be positive"
        ), 400

    result, status_code = purchase_manager.purchase(
        user_id=user["id"],
        product_id=product_id,
        quantity=quantity,
    )

    return jsonify(result), status_code



@app.route("/invoices", methods=["GET"])
def get_invoices():
    user = get_current_user()

    if user is None:
        return jsonify(
            error="Missing, invalid, or expired access token"
        ), 401

    with SessionLocal() as session:
        statement = select(Invoice)

        # Normal users can only see their own invoices.
        # Admins can see invoices from all users.
        if user["role"] != "admin":
            statement = statement.where(
                Invoice.user_id == user["id"]
            )

        statement = statement.order_by(
            Invoice.created_at.desc()
        )

        invoices = session.scalars(statement).all()
        result = []

        for invoice in invoices:
            items_statement = (
                select(InvoiceItem, Product.name)
                .join(
                    Product,
                    InvoiceItem.product_id == Product.id
                )
                .where(InvoiceItem.invoice_id == invoice.id)
            )

            rows = session.execute(items_statement).all()

            items = [
                {
                    "product_id": item.product_id,
                    "product_name": product_name,
                    "quantity": item.quantity,
                    "unit_price": str(item.unit_price),
                }
                for item, product_name in rows
            ]

            result.append({
                "id": invoice.id,
                "user_id": invoice.user_id,
                "created_at": invoice.created_at.isoformat(),
                "total": str(invoice.total),
                "items": items,
            })

        return jsonify(invoices=result), 200




if __name__ == "__main__":
    app.run(debug=True)
