function updateObject(ID, newData){
    fetch("https://api.restful-api.dev/objects/" + ID, {
        method:"PUT",
        body: JSON.stringify(newData),
        headers: {
            "Content-Type": "application/json"
        }
        
    })
    .then(function(response){

        if(!response.ok){
            throw new Error("Unable to update object");
        }

        return response.json()
    })
    .then(function(data){

        console.log(data)

    })
    .catch(function(error){

        if(error.message === "Failed to fetch"){

            console.log("Connection error");

        }
        else{

            console.log(error.message);

        }

    })

}
updateObject("ff8081819d82fab6019e94dd52d93e62", {
    name: "Tablet",
    data: {
        price: 5000
    }
})
