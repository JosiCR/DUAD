/* ==========================================
Admin User
========================================== */

const adminUser = {

    id: "admin-1",

    name: "Administrador",

    email: "admin@lyfter.com",

    password: "admin123",

    role: "admin"

};


/* ==========================================
Initialize Admin User
========================================== */

function initializeAdminUser() {

    const savedAdmin = localStorage.getItem("adminUser");

    if (!savedAdmin) {

        localStorage.setItem("adminUser", JSON.stringify(adminUser));

    }

}


/* ==========================================
Register User
========================================== */

async function registerUser(user) {

    try {

        const response = await axios.post("https://api.restful-api.dev/objects", user);


        const registeredUser = {

            id: response.data.id,

            name: response.data.name,

            email: user.data.email,

            password: user.data.password,

            role: "customer"

        };


        localStorage.setItem("registeredUser", JSON.stringify(registeredUser));


        return {

            success: true,

            data: response.data

        };

    }
    catch (error) {

        let message = "No fue posible registrar el usuario.";

        if (error.response) {

            const status = error.response.status;

            if (status === 400) {

                message = "La información es inválida.";

            }
            else if (status === 404) {

                message = "Recurso no encontrado.";

            }
            else if (status === 500) {

                message = "Error del servidor.";

            }

        }
        else {

            message = "Error de conexión con el servidor.";

        }


        return {

            success: false,

            error: message

        };

    }

}


/* ==========================================
Login User
========================================== */

async function loginUser(email, password) {

    const savedUser = JSON.parse(localStorage.getItem("registeredUser"));

    const savedAdmin = JSON.parse(localStorage.getItem("adminUser"));

    let user = null;


    if (savedAdmin && savedAdmin.email === email) {

        user = savedAdmin;

    }
    else if (savedUser && savedUser.email === email) {

        user = savedUser;

    }


    if (!user) {

        return {

            success: false,

            error: "No existe una cuenta con ese correo."

        };

    }


    if (user.password !== password) {

        return {

            success: false,

            error: "La contraseña es incorrecta."

        };

    }


    return {

        success: true,

        user: user

    };

}


/* ==========================================
Check Session
========================================== */

function checkSession() {

    const currentUser = JSON.parse(localStorage.getItem("currentUser"));

    if (!currentUser) {

        window.location.href = "login.html";

    }

}


/* ==========================================
Check Admin Session
========================================== */

function checkAdminSession() {

    const currentUser = JSON.parse(localStorage.getItem("currentUser"));

    if (!currentUser || currentUser.role !== "admin") {

        alert("No tienes permisos para acceder al panel de administración.");

        window.location.href = "index.html";

    }

}


/* ==========================================
Display Admin Navigation
========================================== */

function displayAdminNavigation() {

    const currentUser = JSON.parse(localStorage.getItem("currentUser"));

    if (!currentUser || currentUser.role !== "admin") {

        return;

    }


    const navigation = document.querySelector("nav");

    if (!navigation) {

        return;

    }


    const existingAdminLink = document.getElementById("adminNavigationLink");

    if (existingAdminLink) {

        return;

    }


    const adminLink = document.createElement("a");

    adminLink.id = "adminNavigationLink";

    adminLink.href = "admin.html";

    adminLink.textContent = "⚙ Administrador";


    navigation.appendChild(adminLink);

}


/* ==========================================
Logout User
========================================== */

function logoutUser() {

    localStorage.removeItem("currentUser");

    window.location.href = "login.html";

}


/* ==========================================
Display Logout Navigation
========================================== */

function displayLogoutNavigation() {

    const currentUser = JSON.parse(localStorage.getItem("currentUser"));

    if (!currentUser) {

        return;

    }


    const navigation = document.querySelector("nav");

    if (!navigation) {

        return;

    }


    const existingLogoutButton = document.getElementById("logoutNavigationButton");

    if (existingLogoutButton) {

        return;

    }


    const logoutButton = document.createElement("button");

    logoutButton.id = "logoutNavigationButton";

    logoutButton.type = "button";

    logoutButton.textContent = "↪ Cerrar sesión";


    logoutButton.addEventListener("click", function () {

        const confirmation = confirm("¿Deseas cerrar la sesión?");

        if (!confirmation) {

            return;

        }

        logoutUser();

    });


    navigation.appendChild(logoutButton);

}


/* ==========================================
Initialize Authentication
========================================== */

initializeAdminUser();

displayAdminNavigation();

displayLogoutNavigation();