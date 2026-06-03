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


function updateObject(ID, newData){
    fetch("https://api.restful-api.dev/objects/" + ID, {
        method:"PUT",
        body: JSON.stringify(newData),
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
updateObject("ff8081819d82fab6019e6b7594100caa", {
    name: "Tablet",
    data: {
        price: 5000
    }
})
