const axios = require("axios");
function listObjects(){
    axios.get("https://api.restful-api.devd/objects")
        .then(function(response){

            if(!Array.isArray(response.data)){
                throw new Error("Invalid response format");
            }

            const onlyData = response.data.filter(function(object){

                return object.data
            })
            onlyData.forEach(function(objectData){

                console.log("ID:", objectData.id);
                console.log("Name:", objectData.name);
                console.log("Data:", objectData.data);
            })
        })
        .catch(function(error){

            if(error.message === "Invalid response format"){

                console.log("Invalid response format");

            }
            else if(error.response){

                if(error.response.status === 404){

                console.log("Resource not found");

                }
                else if(error.response.status >= 500){

                    console.log("Server error");

                }
            }
            else{

                console.log("Connection error");

            }

})
}
listObjects();