// 1. Escribe un comentario en una linea
    // Comentario de una linea

// 2. Escribe un comentario en varias lienas
    /* Comentario de varias lineas */

// 3. Declara variables con valores asociados a todos los datos de tipo primitivo
let nombre = "Jota"
let edad = 37
let eresHumano = true
let eresAnimal = false
let noDefinido 
let valorNulo = null
let simbolo = Symbol("mysymbol")
let numeroEnorme = BigInt(123789124719284719247120984710247)

// 4. Imprime por consola el valor de todas las variables
console.log(nombre)
console.log(edad)
console.log(eresHumano)
console.log(eresAnimal)
console.log(noDefinido)
console.log(valorNulo)
console.log(simbolo)
console.log(numeroEnorme)

// 5. Imprime por consola el tipo de todas las variables
console.log(typeof nombre)
console.log(typeof edad)
console.log(typeof eresHumano)
console.log(typeof eresAnimal)
console.log(typeof noDefinido)
console.log(typeof valorNulo)
console.log(typeof simbolo)
console.log(typeof numeroEnorme)

// 6. A continuacion, modifica los valores de las variables por otros del mismo tipo
nombre = "Pepe"
edad = 27
eresHumano = false
eresAnimal = true
noDefinido = ""
valorNulo =  ""
simbolo = Symbol("no symbol")
numeroEnorme = 98238293829382823982129803123801283102831208312083102n

// 7. A continuacion, modifica los valores de las variables por otros de distinto tipo
nombre = 12
edad = "no define"

// 8. Declara constantes con valores asociados a todos los tipos de datos primitivos
const nombreFijo = "No se puede cambiar"
//nombreFijo = "perfecto dia"
console.log(nombreFijo)

// 9. A conticuacion, modifica los valores de las constantes
// las const no se pueden modificar a no ser que lo usemos como una "function"
const persona = { nombre: "Pepe", ciudad: "Madrid" };
persona.nombre = "Ana"
persona.ciudad = "Valencia"
console.log(persona.nombre, persona.ciudad)

// 10. Comenta las lineas que produzcan algun tipo de error al ejecutarse
/* Las variables const no pueden ser modificadas una ves designadas. 
el error aparece en la linea 53 y desde ahi el codigo se cae*/