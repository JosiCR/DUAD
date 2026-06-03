const loginBtn = document.getElementById("loginBtn");
loginBtn.addEventListener("click", function(){
    const loginId = document.getElementById("loginId").value;
    const loginPassword = document.getElementById("loginPassword").value;

    if(loginId === "" || loginPassword === ""){
        alert("All fields are required");
        return;
    }

    axios.get("https://api.restful-api.dev/objects/" + loginId)
    .then(function(response){
        if(loginPassword === response.data.data.password ){
            localStorage.setItem("userId", loginId);
            window.location.href = "perfil.html";

        }
        else {
            alert("Incorrect password")
        }
    })
    .catch(function(error){
        alert("ID not found")
    })

});