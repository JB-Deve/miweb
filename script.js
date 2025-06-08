
document.getElementById("boton-inicio").addEventListener("click", function(e){
e.preventDefault();

let ingresarInicioUsuario = document.getElementById("ingresa-usuario").value.trim();
let ingresarInicioContra = document.getElementById("ingresa-password").value.trim();

let usuarioValido = "123";
let claveValida = "123";

if (ingresarInicioUsuario === usuarioValido && ingresarInicioContra === claveValida){
    document.getElementById("inicio-login").style.display = "none";
    document.getElementById("seleccionar-pos").style.display = "block";
    
} else {
    alert("Incorrecto!!")
}
});

document.getElementById("cerrar-sesion").addEventListener("click", function(){
    document.getElementById("inicio-login").style.display = "block";
    document.getElementById("seleccionar-pos").style.display = "none";        
});
