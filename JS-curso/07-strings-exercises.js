// 1. Concatena dos cadenas de texto
let dameName = "Jota"
let dameEdad = "Nox"
let tusDatos = dameName + " " + dameEdad

console.log(tusDatos)

// 2. Muestra la longitud de una cadena de texto
console.log(tusDatos.length)

// 3. Muestra el primer y ultimo caracter de un strin
console.log(tusDatos[0], tusDatos[7])

// 4. Convierte a mayusculas y minisculas un string
console.log(tusDatos.toUpperCase())
console.log(tusDatos.toLowerCase())
// 5. Crea una cadena de texto en varias lineas
let textoCadena = `Los textos
en cadena
se pueden crear con
las comillas invertidas.`
console.log(textoCadena)

// 6. Interpola el valor de una variable en un string
let nombre = "nox el mas chingon"
let email = "noxi@hot.com"
console.log(`"Hola, ${nombre}".
"Tu email es: ${email}"`)

// 7. Reemplaza los espacios en blanco de un string por guiones
/*
- Espacios simples .replace(/ /g, "-")
- Para cambiar otros tipos de caracteres .split("o").join("*")
- Reemplazar cualquier tipo de espacios "tabs" (/\s+/g, "-")
*/
let resultado = nombre +" " +email
let resultadoFinal = resultado.split("o").join("*")
console.log(resultadoFinal)

// 8. Comprueba si una cadena de texto contiene una palabra conreta
let contienePalabra = nombre.includes("nox")
console.log(contienePalabra)
// 9. Comprueba si dos strings son iguales

// 10. Comprueba si dos strings tienen la misma longitud

