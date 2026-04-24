const numbers = [1, 2, 3, 4, 5, 6];
const pares = [];

for (let i = 0; i <numbers.length; i++) {
    const num = numbers[i];

    if (num % 2 === 0) {
        pares.push (num);
    }
}

console.log(pares)



//Solucion con filter
const numbers = [5, 12, 19, 20];

const pares = numbers.filter((num) => {
    return num % 2 === 0;
});

console.log(pares);

