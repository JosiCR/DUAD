fetch("https://reqres.in/api/users/2" , {
    headers: {
        "x-api-key":"free_user_3DuUjp72jxMDzc1XzNsX2rjcPsQ"

    }

})
    .then(function(response){

        return response.json();

    })
    .then(function(data){
        console.log(data.data)
    })


    
fetch("https://reqres.in/api/users/23" , {
    headers: {
        "x-api-key":"free_user_3DuUjp72jxMDzc1XzNsX2rjcPsQ"

    }
})
    .then(function(response){

        if(!response.ok){
            throw new Error("User not found");
        }

        return response.json();

    })

    .then(function(data){

        console.log(data.data.first_name, data.data.last_name, data.data.email);

    })

    .catch(function(error){
        console.log("User not found");

    })

    .finally(function(){
        console.log("Request finished")
    })
    
