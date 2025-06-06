
let ingresarInicioUsuario = document.getElementById("ingresar-usuario").value.trim();
let ingresarInicioContra = document.getElementById("ingresar-password").value.trim();

document.getElementById("boton-inicio").addEventListener("click", function(){

let usuarioValido = "mas";
let claveValida = "123";

if (ingresarInicioUsuario === usuarioValido && ingresarInicioContra === claveValida){
    
    alert("Welcome!!");
} else {
    alert("Incorrecto!!")
}

});