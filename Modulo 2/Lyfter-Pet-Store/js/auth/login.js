/* ==========================================
Login Form Elements
========================================== */

const loginForm = document.querySelector("form");

const emailInput = document.getElementById("email");

const passwordInput = document.getElementById("password");

const errorMessage = document.getElementById("errorMessage");


/* ==========================================
Handle Login Form
========================================== */

loginForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    errorMessage.innerHTML = "";

    const errors = [];


    if (emailInput.value.trim() === "") {

        errors.push("El correo electrónico es obligatorio.");

    }
    else {

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailRegex.test(emailInput.value.trim())) {

            errors.push("El correo electrónico no es válido.");

        }

    }


    if (passwordInput.value.trim() === "") {

        errors.push("La contraseña es obligatoria.");

    }


    if (errors.length > 0) {

        errors.forEach(function (error) {

            const errorItem = document.createElement("li");

            errorItem.textContent = error;

            errorMessage.appendChild(errorItem);

        });

        return;

    }


    const result = await loginUser(emailInput.value.trim(), passwordInput.value);


    if (result.success) {

        localStorage.setItem("currentUser", JSON.stringify(result.user));

        window.location.href = "catalog.html";

    }
    else {

        const errorItem = document.createElement("li");

        errorItem.textContent = result.error;

        errorMessage.appendChild(errorItem);

    }

});