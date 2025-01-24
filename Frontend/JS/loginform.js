document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('loginForm');

    form.addEventListener('submit', function(e) {
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

        const [email, password] = inputs;

        if (!email.value.includes('@')) {
            isValid = false;
            email.style.borderColor = 'red';
            alert('Por favor ingrese un email válido');
        }

        if (isValid) {
            // Aquí iría la lógica para enviar el formulario
            console.log('Formulario válido', {
                email: email.value,
                password: password.value
            });
        }
    });

    // Efecto hover para los botones sociales
    const socialButtons = document.querySelectorAll('.social-icon');
    socialButtons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.1)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });
});