/* ==========================================
Initialize Product Form
========================================== */

checkAdminSession();

const urlParameters = new URLSearchParams(window.location.search);

const productId = Number(urlParameters.get("id"));

const isEditing = urlParameters.has("id");

if (isEditing) {

    loadProductInformation();

}


/* ==========================================
Load Product Information
========================================== */

async function loadProductInformation() {

    const result = await getProductById(productId);

    if (!result.success) {

        alert(result.error);

        window.location.href = "admin.html";

        return;

    }


    const product = result.product;


    document.getElementById("formTitle").textContent = "Editar producto";

    document.getElementById("formDescription").textContent = "Modifica la información del producto seleccionado.";

    document.getElementById("saveProductButton").textContent = "Guardar cambios";

    document.getElementById("productName").value = product.name;

    document.getElementById("productCategory").value = product.data.category;

    document.getElementById("productPrice").value = product.data.price;

    document.getElementById("productStock").value = product.data.stock;

    document.getElementById("productImage").value = product.data.image;

    document.getElementById("productDescription").value = product.data.description;

}


/* ==========================================
Handle Product Form
========================================== */

const productForm = document.getElementById("productForm");

productForm.addEventListener("submit", function (event) {

    event.preventDefault();


    const productData = {

        name: document.getElementById("productName").value.trim(),

        category: document.getElementById("productCategory").value.trim(),

        price: Number(document.getElementById("productPrice").value),

        stock: Number(document.getElementById("productStock").value),

        image: document.getElementById("productImage").value.trim(),

        description: document.getElementById("productDescription").value.trim()

    };


    let result;


    if (isEditing) {

        result = updateProduct(productId, productData);

    }
    else {

        result = createProduct(productData);

    }


    if (result.success) {

        alert(result.message);

        window.location.href = "admin.html";

    }
    else {

        alert(result.error);

    }

});


/* ==========================================
Cancel Button
========================================== */

const cancelButton = document.getElementById("cancelButton");

cancelButton.addEventListener("click", function () {

    window.location.href = "admin.html";

});