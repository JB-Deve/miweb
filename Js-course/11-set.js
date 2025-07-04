// Declaracion
let mySet = new Set()
// let mySet2 = {} esto NO es un set
console.log(mySet) 
// Inicializacion
mySet = new Set(["Jota", "Nox", "Ryu", 37, true, "jota@jota.xom"])
console.log(mySet)
//metodos comunes
// ADD and Delete
mySet.add("https://jota.dev") //Agregamos un new element at the end

console.log(mySet)

mySet.delete("https://jota.dev") //Para eliminar tenemos que agregar el nombre exacto

console.log(mySet)

console.log(mySet.delete("Nox")) //Para eliminar tenemos que agregar el nombre exacto
console.log(mySet.delete(4))

console.log(mySet)

//has

console.log(mySet.has("Jota"))
console.log(mySet.has("Nox"))

//size

console.log(mySet.size)

//convertir un SET a ARRAY

let myArray = Array.from(mySet)
console.log(myArray)

//convertir un ARRAY a SET

mySet = new Set(myArray)
console.log(mySet)

// Un SET no admite duplicados como un ARRAY

mySet.add("Nox")
mySet.add("Nox")
mySet.add("Nox")
console.log(mySet)