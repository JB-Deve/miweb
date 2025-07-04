// if, else if, else

let age = 18

if (age == 37) {
    console.log("la edad es 37")
}
else if (age < 18){
    console.log("Es menor de edad")
}
else {
    console.log("Aun no vuelve cuando sea adecuado")
}

// Operadores Ternarios

const message = age == 37 ? "La edad es 37!" : "La edad no es 37!"
console.log(message)

// Swicth - cuando la variable es la misma es mas practico usar Swicth

let day = 3
let dayName

switch (day) {
    case 0:
        dayName = "Lunes"
        break
    case 1:
        dayName = "Martes"
        break
    case 2:
        dayName = "Miercoles"
        break
    case 3:
        dayName = "Jueves"
        break
    case 4:
        dayName = "Viernes"
        break
    case 5:
        dayName = "Sabado"
        break
    case 6:
        dayName = "Domingo"
        break
    default:
        dayName = "Dia incorrecto"
}
console.log(dayName)