const axios = require("axios");
function getObject(ID){
    return axios.get("https://api.restful-api.dev/objects/" + ID)
    .then(function(response){

        return response.data;
    })
    .catch(function(error){

        if(error.response){

            if(error.response.status === 404){

                console.log("Object not found");

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
getObject("ff8081819d82fab6019e6b7594100caa")
    .then(function(data){

        console.log(data);

    });


