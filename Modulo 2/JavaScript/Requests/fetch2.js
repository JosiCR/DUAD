function createObject(objectData){
    fetch("https://api.restful-api.dev/objects", {
        method: "POST",
        body: JSON.stringify(objectData),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(function(response){

        if(!response.ok){

            throw new console.error("Unable to create object");
            return;

        }

        return response.json()
    })
    .then(function(data){
        console.log(data)
    })

    .catch(function(error){
        console.log(error.message);
    })

}
createObject({
    name: "Laptop",
    data:{
        price: 1200
    }
});