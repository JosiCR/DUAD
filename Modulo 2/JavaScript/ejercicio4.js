const example = "This is a string!";
const result = [];

let word = "";

for (let i = 0; i < example.length; i++) {
    const letter = example[i];

    if (letter === "" ) {
        result.push(word);
        word = "";
    } else {
        word += letter;
    }
}

result.push(word);

console.log(result);