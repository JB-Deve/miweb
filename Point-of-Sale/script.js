document.getElementById("seleccionar-pos").style.display = "none";

document.getElementById("boton-inicio").addEventListener("click", function(e){
e.preventDefault();

let ingresarInicioUsuario = document.getElementById("ingresa-usuario").value.trim();
let ingresarInicioContra = document.getElementById("ingresa-password").value.trim();

let usuarioValido = "";
let claveValida = "";

if (ingresarInicioUsuario === usuarioValido && ingresarInicioContra === claveValida){
    document.getElementById("inicio-login").style.display = "none";
    document.getElementById("seleccionar-pos").style.display = "block";
    
} else {
    alert("Incorrecto!!")
}
});
/*
document.getElementById("cerrar-sesion").addEventListener("click", function(){
    let confirmarCerrar = confirm("Confirmar");
    if(confirmarCerrar) {
    document.getElementById("inicio-login").style.display = "block";
    document.getElementById("seleccionar-pos").style.display = "none";     
    }   
});
*/
// CREACION DE MI PRIMER MODAL
function abrirModal() {
    document.getElementById("confirmacion-modal").style.display = "block";
}
function cerrarModal() {
    document.getElementById("confirmacion-modal").style.display = "none";   
}
function confirmar() {
    let confirmarCerraModal = confirmar;
    if(confirmarCerraModal){
    document.getElementById("inicio-login").style.display = "block";
    document.getElementById("seleccionar-pos").style.display = "none";
    cerrarModal();
}

}
/* CREACION DE UN ALERT PERSONALIZADO!!
document.getElementById("cerrar-sesion").addEventListener("click", function () {
  document.getElementById("confirmacion-modal").style.display = "flex";
});

document.getElementById("confirmar-salida").addEventListener("click", function () {
  document.getElementById("inicio-login").style.display = "block";
  document.getElementById("seleccionar-pos").style.display = "none";
  document.getElementById("confirmacion-modal").style.display = "none";
});

document.getElementById("cancelar-salida").addEventListener("click", function () {
  document.getElementById("confirmacion-modal").style.display = "none";
});*/