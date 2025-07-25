// Declaración
let myArray = [] // es recomendado usar esta estructura.
let myArray2 = new Array() //esta estructura suele traer mas errores

console.log(myArray)
console.log(myArray2)

// Inicialización
myArray = [3]
myArray2 = new Array(3) /* reserva el numero de casillas que le metamos
y reserva sus espacios */
console.log(myArray)
console.log(myArray2)

myArray = [1, 2, 3, 4]
myArray2 = new Array(1, 2, 3, 4)

console.log(myArray)
console.log(myArray2)

myArray = ["Brais", "Moure", "mouredev", 37, true]
myArray2 = new Array("Brais", "Moure", "mouredev", 37, true)

console.log(myArray)
console.log(myArray2)

myArray2 = new Array(3)
myArray2[2] = "Brais"
// myArray2[0] = "Moure"
myArray2[1] = "mouredev"
myArray2[4] = "mouredev"
console.log(myArray2)

myArray = []
myArray[2] = "Brais"
// myArray[0] = "Moure"
myArray[1] = "mouredev"

console.log(myArray)

// Métodos comunes
myArray = []

// push y pop
myArray.push("Brais")
myArray.push("Moure")
myArray.push("mouredev")
myArray.push(37)
console.log(myArray)

console.log(myArray.pop()) // Elimina el último y lo devuelve
myArray.pop()
console.log(myArray)

// shift y unshift
console.log(myArray.shift()) //elimina el 1er elemento y lo imprime
console.log(myArray)

myArray.unshift("Brais", "mouredev")
console.log(myArray)

// length
console.log(myArray.length) //imprime cuantos elementos tenemos

// clear
myArray = []
myArray.length = 0 // alternativa, mejor no usarlo
console.log(myArray)

// slice
myArray = ["Brais", "Moure", "mouredev", 37, true]

let myNewArray = myArray.slice(1, 3)//tiene en cuenta el elemento 1 y 2 y no el 3

console.log(myArray)
console.log(myNewArray)

// splice
myArray.splice(1, 3) //elimina desde el 1 al 3
console.log(myArray)

myArray = ["Brais", "Moure", "mouredev", 37, true]

myArray.splice(1, 2, "Nueva entrada")
console.log(myArray)