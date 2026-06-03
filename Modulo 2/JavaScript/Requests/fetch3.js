function getObject(ID){
    fetch("https://api.restful-api.dev/objects/" + ID, {
        
    })
    .then(function(response){
        return response.json()
    })
    .then(function(data){
        console.log(data)
    })

}
getObject(3)