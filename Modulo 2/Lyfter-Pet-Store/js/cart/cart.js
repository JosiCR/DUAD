/* ==========================================
Initialize Cart Page
========================================== */

checkSession();

loadCart();


/* ==========================================
Load Cart
========================================== */

function loadCart() {

    const result = getCart();

    if (result.success) {

        displayCart(result.cart);

        displayCartSummary(result.cart);

    }
    else {

        displayCartError(result.error);

    }

}


/* ==========================================
Display Cart
========================================== */

function displayCart(cart) {

    const cartContainer = document.getElementById("cartContainer");

    cartContainer.innerHTML = "";

    if (cart.length === 0) {

        displayEmptyCart();

        return;

    }

    cart.forEach(function (product) {

        createCartItem(product);

    });

}


/* ==========================================
Create Cart Item
========================================== */

function createCartItem(product) {

    const cartContainer = document.getElementById("cartContainer");


    const article = document.createElement("article");

    article.classList.add("cart-item");


    const image = document.createElement("img");

    image.src = product.data.image;

    image.alt = product.name;

    image.classList.add("cart-item-image");


    const information = document.createElement("div");

    information.classList.add("cart-item-information");


    const title = document.createElement("h3");

    title.textContent = product.name;

    title.classList.add("cart-item-title");


    const category = document.createElement("p");

    category.textContent = product.data.category;

    category.classList.add("cart-item-category");


    const price = document.createElement("p");

    price.textContent = "₡ " + product.data.price;

    price.classList.add("cart-item-price");


    const controls = document.createElement("div");

    controls.classList.add("cart-item-controls");


    const decreaseButton = document.createElement("button");

    decreaseButton.textContent = "−";

    decreaseButton.classList.add("quantity-button");

    decreaseButton.addEventListener("click", function () {

        const result = decreaseCartQuantity(product.id);

        if (result.success) {

            loadCart();

        }
        else {

            alert(result.error);

        }

    });


    const quantity = document.createElement("span");

    quantity.textContent = product.quantity;

    quantity.classList.add("quantity-value");


    const increaseButton = document.createElement("button");

    increaseButton.textContent = "+";

    increaseButton.classList.add("quantity-button");

    increaseButton.addEventListener("click", function () {

        const result = increaseCartQuantity(product.id);

        if (result.success) {

            loadCart();

        }
        else {

            alert(result.error);

        }

    });


    controls.appendChild(decreaseButton);

    controls.appendChild(quantity);

    controls.appendChild(increaseButton);


    const subtotal = document.createElement("p");

    const productSubtotal = product.data.price * product.quantity;

    subtotal.textContent = "Subtotal: ₡ " + productSubtotal.toFixed(2);

    subtotal.classList.add("cart-item-subtotal");


    const removeButton = document.createElement("button");

    removeButton.textContent = "Eliminar";

    removeButton.classList.add("remove-button");

    removeButton.addEventListener("click", function () {

        const result = removeFromCart(product.id);

        if (result.success) {

            loadCart();

        }
        else {

            alert(result.error);

        }

    });


    information.appendChild(title);

    information.appendChild(category);

    information.appendChild(price);

    information.appendChild(controls);


    article.appendChild(image);

    article.appendChild(information);

    article.appendChild(subtotal);

    article.appendChild(removeButton);


    cartContainer.appendChild(article);

}


/* ==========================================
Display Cart Summary
========================================== */

function displayCartSummary(cart) {

    const cartSummary = document.getElementById("cartSummary");

    cartSummary.innerHTML = "";

    if (cart.length === 0) {

        return;

    }


    const title = document.createElement("h3");

    title.textContent = "Resumen de compra";


    const total = cart.reduce(function (accumulator, product) {

        return accumulator + product.data.price * product.quantity;

    }, 0);


    const totalText = document.createElement("p");

    totalText.textContent = "Total: ₡ " + total.toFixed(2);

    totalText.classList.add("cart-total");


    const checkoutButton = document.createElement("button");

    checkoutButton.textContent = "Continuar con la compra";

    checkoutButton.classList.add("checkout-button");

    checkoutButton.addEventListener("click", function () {

        window.location.href = "checkout.html";

    });


    cartSummary.appendChild(title);

    cartSummary.appendChild(totalText);

    cartSummary.appendChild(checkoutButton);

}


/* ==========================================
Display Empty Cart
========================================== */

function displayEmptyCart() {

    const cartContainer = document.getElementById("cartContainer");


    const emptyCart = document.createElement("div");

    emptyCart.classList.add("empty-cart-state");


    const icon = document.createElement("div");

    icon.textContent = "🛒";

    icon.classList.add("cart-state-icon");


    const title = document.createElement("h2");

    title.textContent = "Tu carrito está vacío";


    const description = document.createElement("p");

    description.textContent = "Todavía no has agregado productos. Explora el catálogo y encuentra algo especial para tu mascota.";


    const catalogLink = document.createElement("a");

    catalogLink.href = "catalog.html";

    catalogLink.textContent = "Explorar catálogo";

    catalogLink.classList.add("catalog-button");


    emptyCart.appendChild(icon);

    emptyCart.appendChild(title);

    emptyCart.appendChild(description);

    emptyCart.appendChild(catalogLink);


    cartContainer.appendChild(emptyCart);

}


/* ==========================================
Display Cart Error
========================================== */

function displayCartError(error) {

    const cartContainer = document.getElementById("cartContainer");

    cartContainer.innerHTML = "";


    const message = document.createElement("p");

    message.textContent = error;

    message.classList.add("cart-error-message");


    cartContainer.appendChild(message);

}