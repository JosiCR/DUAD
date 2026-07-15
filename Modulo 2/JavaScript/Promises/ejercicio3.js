const veryPromise = new Promise(function(resolve) {

    setTimeout(function() {

        resolve("very");

    }, 3000);

});
const dogsPromise = new Promise(function(resolve) {

    setTimeout(function() {

        resolve("dogs");

    }, 1000);

});
const cutePromise = new Promise(function(resolve) {

    setTimeout(function() {

        resolve("cute");

    }, 4000);

});
const arePromise = new Promise(function(resolve) {

    setTimeout(function() {

        resolve("are");

    }, 2000);

});


Promise.all([dogsPromise, arePromise, veryPromise, cutePromise])
    .then(function(words){

        console.log(words.join(" "));

    })
