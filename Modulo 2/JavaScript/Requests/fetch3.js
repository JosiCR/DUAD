function getObject(ID){
    return fetch("https://api.restful-api.dev/objects/" + ID,)
    .then(function(response){

    if(!response.ok){
        throw new Error("Object not found");
    }
        
        return response.json()
    })

    .catch(function(error){

        if(error.message === "Failed to fetch"){

            console.log("Connection error");

        }   
        else{

            console.log(error.message);

        }
        throw error;

    })

}
getObject("ff8081819d82fab6019e6b7594100caa")
    .then(function(data){

        console.log(data);

    })
    .catch(function(error){

        console.log("Request failed");

    });