const registerBtn = document.getElementById("registerBtn");
registerBtn.addEventListener("click", function(){

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    console.log(name)
    console.log(email)
    console.log(password)

    if(name ==="" || email === "" || password === ""){
        alert("All fields are required");
        return;
    }

    createObject(name, email, password);
    
})

function createObject(name, email, password){
    axios.post("https://api.restful-api.dev/objects", {
        
        name: name,
        data: {
            email: email,
            password: password
        }
        
    })
    .then(function(response){
        localStorage.setItem("userId", response.data.id);
        alert("User created successfully! Your ID is " + response.data.id)
        window.location.href = "login.html";
    })
    .catch(function(error){
        alert("An error occurred while creating the user")

    })
}


