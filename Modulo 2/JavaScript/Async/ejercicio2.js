async function idUser() {
    try {

        const response = await fetch("https://reqres.in/api/users/23", {
        headers: { 
            "x-api-key": "free_user_3DuUjp72jxMDzc1XzNsX2rjcPsQ"
        }
    })

    if (!response.ok) {
        throw new Error("User not found");
    }

    const data = await response.json();
    console.log(data.data.first_name);
    console.log(data.data.last_name);
    console.log(data.data.email);

    }
    catch(error) {
    console.log("user not found");

    }

}


idUser();