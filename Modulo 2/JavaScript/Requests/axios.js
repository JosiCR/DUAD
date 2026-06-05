const axios = require("axios");
function listObjects(){
    axios.get("https://api.restful-api.dev/objects")
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

            if(error.response){

                console.log("Failed to retrieve objects");


            }
            else{

                console.log("Connection error");

            }

        })
}
listObjects();