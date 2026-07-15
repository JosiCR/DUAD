const fs = require("fs");
const data1 = fs.readFileSync("file1.txt", "utf-8");
const data2 = fs.readFileSync("file2.txt", "utf-8");

const words1 = data1.split("\n");
const words2 = data2.split("\n");

const cleanWords1 = words1.map(word => word.replace("\r", ""))
const cleanWords2 = words2.map(word => word.replace("\r", ""))

const repeated = cleanWords1.filter(word => cleanWords2.includes(word));
console.log(repeated.join(" "));