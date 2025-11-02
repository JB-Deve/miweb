

let myName = "jota"
let greeting = "Hola, " + myName + "!!" 
console.log(greeting)
console.log(typeof greeting)

// Longitud
console.log(greeting.length)

// Acceso a carateres
console.log(greeting[0])
console.log(greeting[11])

// Metodos comunes
console.log(greeting.toUpperCase())
console.log(greeting.toLowerCase())
console.log(greeting.indexOf("Hola"))
console.log(greeting.indexOf("jota"))
console.log(greeting.slice(0, 8))
console.log(greeting.replace("jota", "Nox"))

// Template literals (plantillas literales)

let message = `Hola, este 
es
mi 
practica` // creo una cadena de texto en 2 lineas con las ``
console.log(message)

let email = "pepe@pepito.es"
console.log(`Hola, ${myName}! tu emal es ${email}.`) //interpolacion de variables