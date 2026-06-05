const axios = require("axios");
function createObject(objectData){
    axios.post("https://api.restful-api.dev/objects", objectData)
    .then(function(response){
        console.log(response.data)
    })
    .catch(function(error){

            if(error.response){

                console.log("Failed to create object");


            }
            else{

                console.log("Connection error");

            }

        })


}
createObject({
    name: "Control",
    data: {
        price: 3000
    }
});
