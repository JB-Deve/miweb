// una estructura sirve para almacenar conjunto de datos

//Declaracion

let myMap = new Map()
console.log(myMap)

//inicializacion

myMap = new Map([
    ["name", "Jota"],
    ["email", "jota@jota.com"],
    ["age", 37]
])

console.log(myMap)

//metodos

//set

myMap.set("alias", "pepe")
myMap.set("name", "Jota Big") // no acepta duplicados, reemplaza 

console.log(myMap)

// get - llama a valor que invoquemos

console.log(myMap.get("name"))
console.log(myMap.get("surname"))

//has - llama al valor que invoquemos con true or false

console.log(myMap.has("surname"))
console.log(myMap.has("age"))

//delete

myMap.delete("email")
console.log(myMap)

//size

console.log(myMap.size)

//clear - para eliminar todo el map

myMap.clear()
console.log(myMap)

