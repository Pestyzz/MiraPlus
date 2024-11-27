document.addEventListener('DOMContentLoaded', function() {
    // Ocultar las alertas después de 3 segundos
    setTimeout(function() {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(alert => {
            alert.style.display = 'none';
        });
    }, 3000);
});