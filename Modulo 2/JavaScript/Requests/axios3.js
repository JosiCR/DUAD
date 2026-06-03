const axios = require("axios");
function getObject(ID){
    axios.get("https://api.restful-api.dev/objects/" + ID)
    .then(function(response){
        console.log(response.data)
    })
}
getObject(2)