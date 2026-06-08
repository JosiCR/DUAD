const axios = require("axios");
function updateObject(ID, newData){

    axios.put("https://api.restful-api.dev/objects/" + ID, newData)

    .then(function(response){

        console.log(response.data)

    })
    .catch(function(error){

        if(error.response){

            console.log("Unable to update object");


        }
        else{

            console.log("Connection error");

        }

    })

}
updateObject("ff8081819d82fab6019e6b7594100caa",{
    name: "iphone",
    data: {
        price : 800
    }
});


