// 1. Crea una variable para cada operación aritmetica
let a = 5
let b = 10

console.log(a + b)
// 2. Crea una variable para cada tipo de operacion de asignacion, que haga uso
// de las variables utilizadas para las operaciones aritmeticas.
a *= 5
console.log(a + b)

// 3. Imprime 5 comparaciones verdaderas con diferentes operadores de comparacion
if (a < b){
    console.log("a es menor que b")
} else {
    console.log("a no es menor que b")
}
    
// 4. Imprime 5 comparaciones falsas con diferentes operadores de comparacion
if (a != b){
    console.log("a no es igual a b")
}else {
    console.log("a es igual que b")
}

// 5. Utiliza el operador logico AND
if (a != b && b != a && a > b){
    console.log("positivo tenemos el operador AND en accion")
}else {
    console.log("negativo")
}
// 6. Utiliza el operador logico OR
if (a < b || a > b){
    console.log("positivo es un OR ya que un dato es true")
}else {
    console.log("ambos datos son false")
}
// 7. Combina ambos operadores logicos

// 8. Anade alguna negacion

// 9. Utiliza el operador ternario
const isSunny = false
isSunny ? console.log("Too hot!!") : console.log("Pick up your jacket!!")
// 10. Combina operadores aritmeticos, de comparacion y logicos