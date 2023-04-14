const boton = document.getElementById('boton');
boton.addEventListener('click', validarCambioContrasena);

function validarCambioContrasena() {
    const usuario = document.getElementById('usuario').value;
    const correo = document.getElementById('Correo').value;

    if (usuario.trim() === '') {
        showError('Ingrese su usuario');
    } else if (correo.trim() === '' || !validarCorreo(correo)) {
        showError('Ingrese un correo electrónico válido');
    } else {
        
    }
}

function showError(message) {
    alert(message);
}

function validarCorreo(correo) {
    
    const regexCorreo = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
    return regexCorreo.test(correo);
}
