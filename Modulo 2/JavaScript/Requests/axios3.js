const axios = require("axios");
function getObject(ID){
    return axios.get("https://api.restful-api.dev/objects/" + ID)
    .then(function(response){

        return response.data;
    })
    .catch(function(error){

            if(error.response){

                console.log("Object not found");


            }
            else{

                console.log("Connection error");

            }

            throw error;

        })
}
getObject("ff8081819d82fab6019e94dd52d93e62")
    .then(function(data){

        console.log(data);

    });


