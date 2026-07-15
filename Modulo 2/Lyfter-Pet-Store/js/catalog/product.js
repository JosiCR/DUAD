/* ==========================================
Initialize Product Page
========================================== */

checkSession();

loadProduct();


/* ==========================================
Load Product
========================================== */

async function loadProduct() {

    const params = new URLSearchParams(window.location.search);

    const id = Number(params.get("id"));

    const result = await getProductById(id);

    if (result.success) {

        createProductDetails(result.product);

    }
    else {

        alert(result.error);

    }

}


/* ==========================================
Create Product Details
========================================== */

function createProductDetails(product) {

    const productContainer = document.getElementById("productContainer");

    productContainer.innerHTML = "";


    const article = document.createElement("article");

    article.classList.add("product-card");


    const image = document.createElement("img");

    image.src = product.data.image;

    image.alt = product.name;

    image.classList.add("product-image");


    const information = document.createElement("div");

    information.classList.add("product-information");


    const title = document.createElement("h2");

    title.textContent = product.name;

    title.classList.add("product-title");


    const price = document.createElement("h3");

    price.textContent = "₡ " + product.data.price;

    price.classList.add("product-price");


    const categoryTitle = document.createElement("h4");

    categoryTitle.textContent = "Categoría";


    const category = document.createElement("span");

    category.textContent = product.data.category;

    category.classList.add("product-category");


    const stockTitle = document.createElement("h4");

    stockTitle.textContent = "Disponibilidad";


    const stock = document.createElement("p");

    stock.textContent = "🟢 " + product.data.stock + " unidades disponibles";

    stock.classList.add("product-stock");


    const descriptionTitle = document.createElement("h4");

    descriptionTitle.textContent = "Descripción";


    const description = document.createElement("p");

    description.textContent = product.data.description;

    description.classList.add("product-description");


    const button = document.createElement("button");

    button.textContent = "🛒 Agregar al carrito";

    button.classList.add("primary-button");

    button.addEventListener("click", function () {

        const result = addToCart(product);

        if (result.success) {

            alert(result.message);

        }
        else {

            alert(result.error);

        }

    });


    const backButton = document.createElement("button");

    backButton.textContent = "← Volver al catálogo";

    backButton.classList.add("secondary-button");

    backButton.addEventListener("click", function () {

        window.location.href = "catalog.html";

    });


    information.appendChild(title);

    information.appendChild(price);

    information.appendChild(categoryTitle);

    information.appendChild(category);

    information.appendChild(stockTitle);

    information.appendChild(stock);

    information.appendChild(descriptionTitle);

    information.appendChild(description);

    information.appendChild(button);

    information.appendChild(backButton);


    article.appendChild(image);

    article.appendChild(information);


    productContainer.appendChild(article);

}