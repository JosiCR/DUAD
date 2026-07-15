const userId = localStorage.getItem("userId");

if(userId === null){

    window.location.href = "login.html";

}

axios.get("https://api.restful-api.dev/objects/" + userId)
    .then(function(response){
        const userName = document.getElementById("userName");
        userName.textContent = response.data.name;
        const userEmail = document.getElementById("userEmail");
        userEmail.textContent = response.data.data.email;

    })

const changePasswordBtn = document.getElementById("changePasswordBtn");

changePasswordBtn.addEventListener("click", function(){
    window.location.href = "cambiar-contraseña.html";
});

const logoutBtn = document.getElementById("logoutBtn");
console.log(logoutBtn);
logoutBtn.addEventListener("click", function(){
    localStorage.removeItem("userId");
    window.location.href = "login.html"

})
