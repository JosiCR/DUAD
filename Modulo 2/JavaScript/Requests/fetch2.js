function createObject(name, price){
    fetch("https://api.restful-api.dev/objects", {
        method: "POST",
        body: JSON.stringify({
            name: name,
            data:{
                price:price
            }
        }),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(function(response){
        return response.json()
    })
    .then(function(data){
        console.log(data)
    })

}
createObject("Laptop", 1200)