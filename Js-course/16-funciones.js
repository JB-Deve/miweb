
//Simple
function myFunc() {

    console.log("Holam funcion!")
}
for (let i = 0; i < 5; i++){
    myFunc() //tenemos que invocar la Funcion
}

//con parametros
function myFuncWithParams(name) {
    console.log(`Hola, ${name}!`)
}
myFuncWithParams("Jota")

//Funciones Anonimas

const myFunc2 = function(name) {
    console.log(`Hola, ${name}!`)
}
myFunc2("Jota Big")

// Arrow Functions
const myFunc3 = (name) => {
    console.log(`Hola, ${name}!`)
}
const myFunc4 = (name) => console.log(`Hi, ${name}!`) // forma simplificada
myFunc3("Jota Big")
myFunc4("Jota el Big")

// PARAMETROS

function sum(a, b) {
    console.log(a + b)
}
sum(5, 10)
sum(5)
sum()

function defaultSum(a = 0, b = 0) {
    console.log(a + b)
}

// valores por defecto

defaultSum()
defaultSum(5)
defaultSum(5, 10)
defaultSum(b = 5)

//retorno de valores

function mult(a, b) {
    return a * b
}
let result = mult(5, 10)
console.log(result)

//funciones anidadas

function extern() {
    console.log("Funcion externa")
    function intern(){
        console.log("Funcion interna")
    }
    intern() // esta es la manera de llamarlo desde adentro
}
extern()
// inter() - da error por que esta fuera de su scoop

//funciones de orden superior

function applyFunc(func, param) {
    func(param)
}
applyFunc(myFunc4, "Funcion de orden superior")

//forEach - 

const myArray = [1, 2, 3, 4]

const mySet = new Set(["Brais", "Moure", "mouredev", 37, true, "braismoure@mouredev.com"])

const myMap = new Map([
    ["name", "Brais"],
    ["email", "braismoure@mouredev.com"],
    ["age", 37]
])

myArray.forEach(function (value) {
    console.log(value)
})

myArray.forEach((value) => console.log(value))

mySet.forEach((value) => console.log(value))

myMap.forEach((value) => console.log(value))

