const axios = require("axios");
axios.get("https://api.restful-api.dev/objects")
    .then(function(response){
        const onlyData = response.data.filter(function(object){

            return object.data
        })
            onlyData.forEach(function(objectData){

                console.log(objectData);
            })
    })
