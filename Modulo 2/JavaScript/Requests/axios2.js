const axios = require("axios");
function createObject(name, price){
    axios.post("https://api.restful-api.dev/objects", {
    name: name,
    data: {
        price: price
    }

    })
    .then(function(response){
        console.log(response.data)
    })


}
createObject("Control", 3000)
