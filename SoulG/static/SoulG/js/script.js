const formulario = document.querySelector('form');

formulario.addEventListener('submit', function(event) {
  event.preventDefault(); 

  const usuario = document.querySelector('#Usuario').value.trim();
  const email = document.querySelector('#email').value.trim();
  const password = document.querySelector('#password').value.trim();
  const password2 = document.querySelector('#password2').value.trim();
  const direccion = document.querySelector('#Direccion').value.trim();


  if (usuario === '') {
    alert('Por favor ingrese un usuario');
    return;
  }

  if (email === '') {
    alert('Por favor ingrese un correo electrónico');
    return;
  } else if (!/\S+@\S+.\S+/.test(email)) {
    alert('Por favor ingrese un correo electrónico válido');
    return;
  }

  if (password === '') {
    alert('Por favor ingrese una contraseña');
    return;
  } else if (password.length < 6) {
    alert('La contraseña debe tener al menos 6 caracteres');
    return;
  }


  if (password2 === '') {
    alert('Por favor repita la contraseña');
    return;
  } else if (password !== password2) {
    alert('Las contraseñas no coinciden');
    return;
  }


  if (direccion === '') {
    alert('Por favor ingrese una dirección');
    return;
  }


  alert('Formulario enviado correctamente');
  formulario.submit();
});