const pokemon1 = fetch('https://pokeapi.co/api/v2/pokemon/151');
const pokemon2 = fetch('https://pokeapi.co/api/v2/pokemon/384');
const pokemon3 = fetch('https://pokeapi.co/api/v2/pokemon/658');


Promise.all([pokemon1, pokemon2, pokemon3])
    .then(function(responses){
        const data = responses.map(responses => responses.json());

        Promise.all(data)
            .then(function(pokemons) {
                console.log(pokemons[0].name, pokemons[1].name, pokemons[2].name);

            });

    });

