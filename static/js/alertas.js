document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    const messagesContainer = document.getElementById('messages-container');

    // Si no hay alertas, salir
    if (alerts.length === 0) return;

    alerts.forEach(alert => {
        // Configurar cierre automático después de 4 segundos
        const autoCloseTimer = setTimeout(() => {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            bsAlert.close();
        }, 4000);

        // Manejar cierre manual o automático
        alert.addEventListener('closed.bs.alert', function() {
            // Limpiar el temporizador si el usuario cierra manualmente
            clearTimeout(autoCloseTimer);
            
            // Eliminar la alerta
            this.remove();
            
            // Verificar si quedan más alertas
            const remainingAlerts = document.querySelectorAll('.alert');
            if (remainingAlerts.length === 0 && messagesContainer) {
                messagesContainer.remove();
            }
        });
    });
});