/* ==========================================
Initialize Admin Page
========================================== */

checkAdminSession();

loadAdminProducts();

loadOrders();


/* ==========================================
Load Admin Products
========================================== */

async function loadAdminProducts() {

    const result = await getProducts();

    if (result.success) {

        displayAdminProducts(result.products);

    }
    else {

        displayAdminMessage(result.error, "error");

    }

}


/* ==========================================
Display Admin Products
========================================== */

function displayAdminProducts(products) {

    const productsTableBody = document.getElementById("productsTableBody");

    productsTableBody.innerHTML = "";


    if (products.length === 0) {

        displayAdminMessage("No existen productos registrados.", "information");

        return;

    }


    products.forEach(function (product) {

        createProductRow(product);

    });

}


/* ==========================================
Create Product Row
========================================== */

function createProductRow(product) {

    const productsTableBody = document.getElementById("productsTableBody");


    const row = document.createElement("tr");


    const productCell = document.createElement("td");


    const productInformation = document.createElement("div");

    productInformation.classList.add("admin-product-information");


    const image = document.createElement("img");

    image.src = product.data.image;

    image.alt = product.name;

    image.classList.add("admin-product-image");


    const name = document.createElement("span");

    name.textContent = product.name;

    name.classList.add("admin-product-name");


    productInformation.appendChild(image);

    productInformation.appendChild(name);


    productCell.appendChild(productInformation);


    const categoryCell = document.createElement("td");

    categoryCell.textContent = product.data.category;


    const priceCell = document.createElement("td");

    priceCell.textContent = "₡ " + product.data.price.toFixed(2);


    const stockCell = document.createElement("td");

    stockCell.textContent = product.data.stock;


    const actionsCell = document.createElement("td");

    actionsCell.classList.add("admin-actions");


    const editButton = document.createElement("button");

    editButton.textContent = "✏ Editar";

    editButton.classList.add("edit-product-button");


    editButton.addEventListener("click", function () {

        window.location.href = "edit-product.html?id=" + product.id;

    });


    const deleteButton = document.createElement("button");

    deleteButton.textContent = "🗑 Eliminar";

    deleteButton.classList.add("delete-product-button");


    deleteButton.addEventListener("click", function () {

        const confirmation = confirm("¿Deseas eliminar el producto \"" + product.name + "\"?");


        if (!confirmation) {

            return;

        }


        const result = deleteProduct(product.id);


        if (result.success) {

            displayAdminMessage(result.message, "success");

            loadAdminProducts();

        }
        else {

            displayAdminMessage(result.error, "error");

        }

    });


    actionsCell.appendChild(editButton);

    actionsCell.appendChild(deleteButton);


    row.appendChild(productCell);

    row.appendChild(categoryCell);

    row.appendChild(priceCell);

    row.appendChild(stockCell);

    row.appendChild(actionsCell);


    productsTableBody.appendChild(row);

}


/* ==========================================
Load Orders
========================================== */

function loadOrders() {

    const orders = JSON.parse(localStorage.getItem("orders")) || [];

    displayOrders(orders);

}


/* ==========================================
Display Orders
========================================== */

function displayOrders(orders) {

    const ordersTableBody = document.getElementById("ordersTableBody");

    ordersTableBody.innerHTML = "";


    if (orders.length === 0) {

        displaySalesMessage("No existen ventas registradas.", "information");

        return;

    }


    displaySalesMessage("", "");


    const newestOrders = orders.slice().reverse();


    newestOrders.forEach(function (order) {

        createOrderRow(order);

    });

}


/* ==========================================
Create Order Row
========================================== */

function createOrderRow(order) {

    const ordersTableBody = document.getElementById("ordersTableBody");


    const row = document.createElement("tr");


    const orderCell = document.createElement("td");

    orderCell.textContent = "#" + order.id.toString().slice(-6);

    orderCell.classList.add("order-id");


    const customerCell = document.createElement("td");


    const customerInformation = document.createElement("div");

    customerInformation.classList.add("order-customer-information");


    const customerName = document.createElement("span");

    customerName.textContent = order.customer;

    customerName.classList.add("order-customer-name");


    const customerEmail = document.createElement("span");

    customerEmail.textContent = order.email;

    customerEmail.classList.add("order-customer-email");


    customerInformation.appendChild(customerName);

    customerInformation.appendChild(customerEmail);


    customerCell.appendChild(customerInformation);


    const dateCell = document.createElement("td");

    dateCell.textContent = order.date;


    const productsCell = document.createElement("td");


    const productsList = document.createElement("div");

    productsList.classList.add("order-products");


    order.products.forEach(function (product) {

        const productText = document.createElement("span");

        productText.textContent = product.quantity + " × " + product.name;

        productsList.appendChild(productText);

    });


    productsCell.appendChild(productsList);


    const totalCell = document.createElement("td");

    totalCell.textContent = "₡ " + order.total.toFixed(2);

    totalCell.classList.add("order-total");


    row.appendChild(orderCell);

    row.appendChild(customerCell);

    row.appendChild(dateCell);

    row.appendChild(productsCell);

    row.appendChild(totalCell);


    ordersTableBody.appendChild(row);

}


/* ==========================================
Create Product Button
========================================== */

const createProductButton = document.getElementById("createProductButton");


createProductButton.addEventListener("click", function () {

    window.location.href = "edit-product.html";

});


/* ==========================================
Display Admin Message
========================================== */

function displayAdminMessage(message, type) {

    const adminMessage = document.getElementById("adminMessage");

    adminMessage.textContent = message;

    adminMessage.className = "admin-message " + type;

}


/* ==========================================
Display Sales Message
========================================== */

function displaySalesMessage(message, type) {

    const salesMessage = document.getElementById("salesMessage");

    salesMessage.textContent = message;

    salesMessage.className = "admin-message " + type;

}