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

        updateObject(response.data.id, {
            name: "Wii",
            data: {
                price: 4500
            }
        })

    })

}

function updateObject(ID, newData){

    axios.put("https://api.restful-api.dev/objects/" + ID, newData)

    .then(function(response){

        console.log(response.data)

    })

}

createObject("Control", 3000)

