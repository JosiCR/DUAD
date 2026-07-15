function checkNumber (number, evenCallback, oddCallback) {
    if (number % 2 === 0) {
        evenCallback();
    } else {
        oddCallback();
    }


}


function evenMessage(){
    console.log("The number is even")
}


function oddMessage(){
    console.log("The number is odd")
}

checkNumber(23, evenMessage, oddMessage);