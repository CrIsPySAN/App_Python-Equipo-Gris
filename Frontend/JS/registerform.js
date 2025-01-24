document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('registerForm');

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const inputs = this.querySelectorAll('input');
        let isValid = true;

        inputs.forEach(input => {
            if (!input.value) {
                isValid = false;
                input.style.borderColor = 'red';
            } else {
                input.style.borderColor = '';
            }
        });

        const [username, email, password, confirmPassword] = inputs;

        if (password.value !== confirmPassword.value) {
            isValid = false;
            password.style.borderColor = 'red';
            confirmPassword.style.borderColor = 'red';
            alert('Las contraseñas no coinciden');
        }

        if (!email.value.includes('@')) {
            isValid = false;
            email.style.borderColor = 'red';
            alert('Por favor ingrese un email válido');
        }

        if (isValid) {
            // Aquí iría la lógica para enviar el formulario
            console.log('Formulario válido', {
                username: username.value,
                email: email.value,
                password: password.value
            });
        }
    });
});