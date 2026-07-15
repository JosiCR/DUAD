/* ==========================================
Initialize Checkout Page
========================================== */

checkSession();

loadCheckout();


/* ==========================================
Load Checkout
========================================== */

function loadCheckout() {

    const result = getCart();

    if (!result.success) {

        displayCheckoutError(result.error);

        return;

    }

    if (result.cart.length === 0) {

        window.location.href = "cart.html";

        return;

    }

    displayCheckoutSummary(result.cart);

}


/* ==========================================
Display Checkout Summary
========================================== */

function displayCheckoutSummary(cart) {

    const checkoutSummary = document.getElementById("checkoutSummary");

    checkoutSummary.innerHTML = "";


    const title = document.createElement("h3");

    title.textContent = "Resumen del pedido";


    const productsContainer = document.createElement("div");

    productsContainer.classList.add("checkout-products");


    cart.forEach(function (product) {

        const productItem = document.createElement("div");

        productItem.classList.add("checkout-product");


        const productInformation = document.createElement("div");

        productInformation.classList.add("checkout-product-information");


        const productName = document.createElement("p");

        productName.textContent = product.name;

        productName.classList.add("checkout-product-name");


        const productQuantity = document.createElement("span");

        productQuantity.textContent = "Cantidad: " + product.quantity;

        productQuantity.classList.add("checkout-product-quantity");


        const productSubtotal = document.createElement("p");

        const subtotal = product.data.price * product.quantity;

        productSubtotal.textContent = "₡ " + subtotal.toFixed(2);

        productSubtotal.classList.add("checkout-product-subtotal");


        productInformation.appendChild(productName);

        productInformation.appendChild(productQuantity);


        productItem.appendChild(productInformation);

        productItem.appendChild(productSubtotal);


        productsContainer.appendChild(productItem);

    });


    const total = calculateCartTotal(cart);


    const totalContainer = document.createElement("div");

    totalContainer.classList.add("checkout-total-container");


    const totalTitle = document.createElement("p");

    totalTitle.textContent = "Total";


    const totalPrice = document.createElement("p");

    totalPrice.textContent = "₡ " + total.toFixed(2);

    totalPrice.classList.add("checkout-total");


    totalContainer.appendChild(totalTitle);

    totalContainer.appendChild(totalPrice);


    checkoutSummary.appendChild(title);

    checkoutSummary.appendChild(productsContainer);

    checkoutSummary.appendChild(totalContainer);

}


/* ==========================================
Calculate Cart Total
========================================== */

function calculateCartTotal(cart) {

    return cart.reduce(function (total, product) {

        return total + product.data.price * product.quantity;

    }, 0);

}


/* ==========================================
Update Product Stock
========================================== */

function updateProductStock(cart) {

    const products = JSON.parse(localStorage.getItem("products")) || [];


    for (const cartProduct of cart) {

        const product = products.find(function (product) {

            return product.id === cartProduct.id;

        });


        if (!product) {

            return {
                success: false,
                error: "Uno de los productos ya no existe."
            };

        }


        if (product.data.stock < cartProduct.quantity) {

            return {
                success: false,
                error: "No hay suficientes unidades disponibles de " + product.name + "."
            };

        }

    }


    cart.forEach(function (cartProduct) {

        const product = products.find(function (product) {

            return product.id === cartProduct.id;

        });

        product.data.stock -= cartProduct.quantity;

    });


    localStorage.setItem("products", JSON.stringify(products));


    return {
        success: true
    };

}


/* ==========================================
Handle Checkout Form
========================================== */

const checkoutForm = document.getElementById("checkoutForm");

checkoutForm.addEventListener("submit", function (event) {

    event.preventDefault();


    const result = getCart();


    if (!result.success || result.cart.length === 0) {

        alert("El carrito está vacío.");

        window.location.href = "cart.html";

        return;

    }


    const stockResult = updateProductStock(result.cart);


    if (!stockResult.success) {

        alert(stockResult.error);

        return;

    }


    const fullName = document.getElementById("fullName").value.trim();

    const email = document.getElementById("email").value.trim();

    const phone = document.getElementById("phone").value.trim();

    const address = document.getElementById("address").value.trim();


    const total = calculateCartTotal(result.cart);


    const orders = JSON.parse(localStorage.getItem("orders")) || [];


    const order = {

        id: Date.now(),

        customer: fullName,

        email: email,

        phone: phone,

        address: address,

        date: new Date().toLocaleString("es-CR"),

        products: result.cart,

        total: total

    };


    orders.push(order);


    localStorage.setItem("orders", JSON.stringify(orders));

    localStorage.setItem("lastOrder", JSON.stringify(result.cart));

    localStorage.removeItem("cart");

    window.location.href = "purchase-completed.html";

});


/* ==========================================
Display Checkout Error
========================================== */

function displayCheckoutError(error) {

    const checkoutSummary = document.getElementById("checkoutSummary");


    const message = document.createElement("p");

    message.textContent = error;

    message.classList.add("checkout-error-message");


    checkoutSummary.appendChild(message);

}