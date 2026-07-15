/* ==========================================
Register Form Elements
========================================== */

const registerForm = document.getElementById("registerForm");

const nameInput = document.getElementById("name");

const emailInput = document.getElementById("email");

const passwordInput = document.getElementById("password");

const confirmPasswordInput = document.getElementById("confirmPassword");

const errorMessage = document.getElementById("errorMessage");


/* ==========================================
Handle Register Form
========================================== */

registerForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    errorMessage.innerHTML = "";

    const errors = [];


    if (nameInput.value.trim() === "") {

        errors.push("El nombre es obligatorio.");

    }


    if (emailInput.value.trim() === "") {

        errors.push("El correo electrónico es obligatorio.");

    }
    else {

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailRegex.test(emailInput.value.trim())) {

            errors.push("El correo electrónico no es válido.");

        }

    }


    if (passwordInput.value.length < 8) {

        errors.push("La contraseña debe tener al menos 8 caracteres.");

    }


    if (passwordInput.value !== confirmPasswordInput.value) {

        errors.push("Las contraseñas no coinciden.");

    }


    if (errors.length > 0) {

        errors.forEach(function (error) {

            const errorItem = document.createElement("li");

            errorItem.textContent = error;

            errorMessage.appendChild(errorItem);

        });

        return;

    }


    const user = {

        name: nameInput.value.trim(),

        data: {

            email: emailInput.value.trim(),

            password: passwordInput.value

        }

    };


    const result = await registerUser(user);


    if (result.success) {

        window.location.href = "login.html";

    }
    else {

        const errorItem = document.createElement("li");

        errorItem.textContent = result.error;

        errorMessage.appendChild(errorItem);

    }

});