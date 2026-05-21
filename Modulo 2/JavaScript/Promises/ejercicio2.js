const pokemon1 = fetch('https://pokeapi.co/api/v2/pokemon/151');
const pokemon2 = fetch('https://pokeapi.co/api/v2/pokemon/384');
const pokemon3 = fetch('https://pokeapi.co/api/v2/pokemon/658');


Promise.any([pokemon1, pokemon2, pokemon3])
    .then(function(response){
        return response.json();

    })
    .then(function(pokemon){
        console.log(pokemon.name)

    });