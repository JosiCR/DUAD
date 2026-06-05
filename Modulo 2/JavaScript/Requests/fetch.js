function listObjects(){
    fetch("https://api.restful-api.dev/objects")

    .then(function(response){

        if(!response.ok){
            console.log("Error retrieving objects")
        }

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
    .catch(function(error){

        console.log("Unable to retrieve objects");

    })

}

listObjects();

    