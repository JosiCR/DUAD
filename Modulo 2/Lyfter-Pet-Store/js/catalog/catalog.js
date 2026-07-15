/* ==========================================
Initialize Catalog
========================================== */

const currentUser = JSON.parse(localStorage.getItem("currentUser"));

let allProducts = [];

if (currentUser) {

    loadProducts();

}
else {

    displayLoginRequired();

}


/* ==========================================
Load Products
========================================== */

async function loadProducts() {

    const result = await getProducts();

    if (result.success) {

        allProducts = result.products;

        if (allProducts.length === 0) {

            displayEmptyCatalog();

            return;

        }

        displayProducts(allProducts);

    }
    else {

        displayEmptyCatalog();

    }

}


/* ==========================================
Display Products
========================================== */

function displayProducts(products) {

    const productsContainer = document.getElementById("productsContainer");

    productsContainer.innerHTML = "";

    if (products.length === 0) {

        displayNoResults();

        return;

    }

    products.forEach(function (product) {

        createProductCard(product);

    });

}


/* ==========================================
Create Product Card
========================================== */

function createProductCard(product) {

    const productsContainer = document.getElementById("productsContainer");

    const article = document.createElement("article");

    article.style.cursor = "pointer";

    article.addEventListener("click", function () {

        window.location.href = "product.html?id=" + product.id;

    });


    const image = document.createElement("img");

    image.src = product.data.image;

    image.alt = product.name;


    const title = document.createElement("h3");

    title.textContent = product.name;


    const category = document.createElement("p");

    category.textContent = "Categoría: " + product.data.category;


    const price = document.createElement("p");

    price.textContent = "₡ " + product.data.price;


    const stock = document.createElement("p");

    stock.textContent = "Stock: " + product.data.stock;


    const button = document.createElement("button");

    button.textContent = "Agregar al carrito";

    button.addEventListener("click", function (event) {

        event.stopPropagation();

        const result = addToCart(product);

        if (result.success) {

            alert(result.message);

        }
        else {

            alert(result.error);

        }

    });


    article.appendChild(image);

    article.appendChild(title);

    article.appendChild(category);

    article.appendChild(price);

    article.appendChild(stock);

    article.appendChild(button);


    productsContainer.appendChild(article);

}


/* ==========================================
Filter Products
========================================== */

function filterProducts() {

    const searchValue = document.getElementById("searchInput").value.trim().toLowerCase();

    const selectedCategory = document.getElementById("categoryFilter").value;


    const filteredProducts = allProducts.filter(function (product) {

        const matchesSearch = product.name.toLowerCase().includes(searchValue);

        const matchesCategory = selectedCategory === "" || product.data.category === selectedCategory;

        return matchesSearch && matchesCategory;

    });


    displayProducts(filteredProducts);

}


/* ==========================================
Search Input
========================================== */

const searchInput = document.getElementById("searchInput");

searchInput.addEventListener("input", function () {

    filterProducts();

});


/* ==========================================
Category Filter
========================================== */

const categoryFilter = document.getElementById("categoryFilter");

categoryFilter.addEventListener("change", function () {

    filterProducts();

});


/* ==========================================
Display Login Required
========================================== */

function displayLoginRequired() {

    const catalogFilters = document.getElementById("catalogFilters");

    const productsContainer = document.getElementById("productsContainer");

    catalogFilters.style.display = "none";

    productsContainer.innerHTML = "";


    const loginRequired = document.createElement("div");

    loginRequired.classList.add("catalog-login-required");


    const icon = document.createElement("div");

    icon.classList.add("catalog-state-icon");

    icon.textContent = "🔒";


    const title = document.createElement("h2");

    title.textContent = "Inicia sesión para continuar";


    const description = document.createElement("p");

    description.textContent = "Accede a tu cuenta para explorar nuestros productos y agregar artículos al carrito.";


    const loginLink = document.createElement("a");

    loginLink.href = "login.html";

    loginLink.textContent = "Iniciar sesión";

    loginLink.classList.add("catalog-login-button");


    const registerText = document.createElement("p");

    registerText.classList.add("catalog-register-text");

    registerText.textContent = "¿Todavía no tienes una cuenta? ";


    const registerLink = document.createElement("a");

    registerLink.href = "register.html";

    registerLink.textContent = "Regístrate";


    registerText.appendChild(registerLink);


    loginRequired.appendChild(icon);

    loginRequired.appendChild(title);

    loginRequired.appendChild(description);

    loginRequired.appendChild(loginLink);

    loginRequired.appendChild(registerText);


    productsContainer.appendChild(loginRequired);

}


/* ==========================================
Display Empty Catalog
========================================== */

function displayEmptyCatalog() {

    const catalogFilters = document.getElementById("catalogFilters");

    const productsContainer = document.getElementById("productsContainer");

    catalogFilters.style.display = "none";

    productsContainer.innerHTML = "";


    const emptyCatalog = document.createElement("div");

    emptyCatalog.classList.add("catalog-empty-state");


    const icon = document.createElement("div");

    icon.classList.add("catalog-state-icon");

    icon.textContent = "📦";


    const title = document.createElement("h2");

    title.textContent = "No hay productos disponibles";


    const description = document.createElement("p");

    description.textContent = "Actualmente no existen productos disponibles en el catálogo. Vuelve más tarde para descubrir nuevos artículos.";


    const homeLink = document.createElement("a");

    homeLink.href = "index.html";

    homeLink.textContent = "Volver al inicio";

    homeLink.classList.add("catalog-state-button");


    emptyCatalog.appendChild(icon);

    emptyCatalog.appendChild(title);

    emptyCatalog.appendChild(description);

    emptyCatalog.appendChild(homeLink);


    productsContainer.appendChild(emptyCatalog);

}


/* ==========================================
Display No Results
========================================== */

function displayNoResults() {

    const productsContainer = document.getElementById("productsContainer");

    productsContainer.innerHTML = "";


    const noResults = document.createElement("div");

    noResults.classList.add("catalog-empty-state");


    const icon = document.createElement("div");

    icon.classList.add("catalog-state-icon");

    icon.textContent = "🔍";


    const title = document.createElement("h2");

    title.textContent = "No encontramos productos";


    const description = document.createElement("p");

    description.textContent = "Intenta utilizar otro nombre o seleccionar una categoría diferente.";


    const clearButton = document.createElement("button");

    clearButton.type = "button";

    clearButton.textContent = "Limpiar filtros";

    clearButton.classList.add("catalog-state-button");

    clearButton.addEventListener("click", function () {

        searchInput.value = "";

        categoryFilter.value = "";

        displayProducts(allProducts);

    });


    noResults.appendChild(icon);

    noResults.appendChild(title);

    noResults.appendChild(description);

    noResults.appendChild(clearButton);


    productsContainer.appendChild(noResults);

}