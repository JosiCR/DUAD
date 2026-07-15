async function idUser() {
    const response = await fetch("https://reqres.in/api/users/2", {
        headers: { 
            "x-api-key": "free_user_3DuUjp72jxMDzc1XzNsX2rjcPsQ"

        }
    })
    const data = await response.json();
    console.log(data.data.first_name);
    console.log(data.data.last_name);
    console.log(data.data.email);
}


idUser();