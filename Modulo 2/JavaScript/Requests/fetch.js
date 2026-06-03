fetch("https://api.restful-api.dev/objects")

    .then(function(response){

        return response.json();
    })

    .then(function(data){
        const onlyData = data.filter(function(object){

            return object.data
        })
        onlyData.forEach(function(objectData){

            console.log(objectData);
        })
    })

    