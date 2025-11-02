// Operadores aritmeticos

let a = 5
let b = 10

console.log(a + b)
console.log(a - b)
console.log(a * b)
console.log(a / b)

console.log(a % b)  //Modulo (el resto de la division)
console.log(a ** b) //Exponente

a++ // Incremento
console.log(a)
b-- // Decremento
console.log(b)

// Operadores de asignacion

let myVariable = 5
console.log(myVariable)
myVariable += 2 //(+= coge el valor asignado y le suma 2, se puede usar para todo)
console.log(myVariable)

// Operadores de comparacion

console.log(a > b)
console.log(a < b)
console.log(a >= b)
console.log(a <= b)
console.log(a == b)
console.log(a == 6) //Igualdad por valor (toma igual al los numeros en "6")
console.log(a == a)
console.log(a === a) // Igualdad por identidad (por tipo y valor) 
console.log(a != 6)
console.log(a !== "6")

/* ------------------------
   ---OPERADORES LOGICOS---
   ------------------------ */

//AND (&&)
console.log(5 > 10 && 15 > 20)
console.log(5 < 10 && 15 < 20)
console.log(5 < 10 && 15 > 20)
console.log(5 > 10 && 15 > 20 && 30 > 40)

//OR (||)
console.log(5 > 10 || 15 > 20)
console.log(5 < 10 || 15 < 20)
console.log(5 < 10 || 15 > 20)
console.log(5 > 10 || 15 > 20 || 30 > 40)

console.log(5 > 10 && 15 > 20 || 30 < 40)

//NOT (!)
console.log(!true)
console.log(!false)
console.log(!(5 > 10 && 15 > 20))
console.log(!(5 > 10 || 15 > 20))

//OPERADORES TERNARIOS
const isRaining = true

isRaining ? console.log("Esta lloviendo") : console.log("No esta lloviendo")