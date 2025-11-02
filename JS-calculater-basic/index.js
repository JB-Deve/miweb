let num1 = 8
let num2 = 2

document.getElementById("num1-el").textContent = num1
document.getElementById("num2-el").textContent = num2

//create four functions: add(), substract(), divide(), multiply()
//call the correct function when call by buttons
//ADD
let sumEl = document.getElementById("sum-el")

function add() {
    let resul = num1 + num2
    sumEl.textContent = "sum: " + resul
    console.log(sumEl)
}

//SUBSTRACT
function subtract() {
    let resul = num1 - num2
    sumEl.textContent = "substraction: " + resul
    console.log(sumEl)
}

//DIVIDE
function divide() {
    let resul = num1 / num2
    sumEl.textContent = "division: " + resul
    console.log(sumEl)
}

//MULTIPLY
function multiply() {
    let resul = num1 * num2
    sumEl.textContent = "multiplication: " + resul
    console.log(sumEl)
}

