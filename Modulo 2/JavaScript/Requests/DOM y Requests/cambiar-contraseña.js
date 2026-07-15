const changeBtn = document.getElementById("changeBtn");
changeBtn.addEventListener("click", function(){
    const id = document.getElementById("id").value;
    const oldPassword = document.getElementById("oldPassword").value;
    const newPassword = document.getElementById("newPassword").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    if(id === "" || oldPassword === "" || newPassword === "" || confirmPassword === ""){
        alert("All fields are required");
        return;
    }   
    if(newPassword !== confirmPassword){
        alert("New passwords do not match");
        return;
    }
console.log(id);
axios.get("https://api.restful-api.dev/objects/" + id)
    .then(function(response){
        if(oldPassword !== response.data.data.password){
            alert("Incorrect Password");
            return;
        }
        axios.put("https://api.restful-api.dev/objects/" + id, {

            name: response.data.name,
            data:{
                email: response.data.data.email,
                password: newPassword

            }
        })
        .then(function(response){
            alert("Password updated successfully");
            window.location.href = "login.html";
        })
    })
    .catch(function(error){
        alert("User not found");
    })
})