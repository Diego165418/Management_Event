// document.addEventListener('DOMContentLoaded', function () {
//     var messagesData = document.getElementById('messages-data').textContent;
//     var messages = JSON.parse(messagesData || '[]');
//     if (messages.length > 0) {
//         var modalMessage = document.getElementById('modalMessage');
//         modalMessage.innerHTML = messages.map(msg => `
//             <div class="alert alert-info">${msg}</div>
//         `).join('');
//         var messageModal = new bootstrap.Modal(document.getElementById('messageModal'));
//         messageModal.show();
//     }
// });
// document.addEventListener('DOMContentLoaded', function() {
//     const messageModal = document.getElementById('messageModal');
//     const messages = document.getElementById('messages');
    
//     if (messageModal && messages) {
//         // Si el modal y los mensajes existen, muestra el modal
//         if (messages.dataset.hasMessages === 'true') {
//             const bootstrapModal = new bootstrap.Modal(messageModal);
//             bootstrapModal.show();
//         }
//     }
// });
document.addEventListener('DOMContentLoaded', function () {
    // Obtiene los mensajes desde el script de datos
    var messagesData = document.getElementById('messages-data').textContent;
    
    // Intenta analizar los mensajes JSON
    var messages = [];
    try {
        messages = JSON.parse(messagesData || '[]');
    } catch (e) {
        console.error('Error parsing messages:', e);
    }

    // Verifica si hay mensajes para mostrar
    if (messages.length > 0) {
        var modalMessage = document.getElementById('modalMessage');
        modalMessage.innerHTML = messages.map(msg => `
            <div class="alert alert-info">${msg}</div>
        `).join('');
        
        var messageModal = new bootstrap.Modal(document.getElementById('messageModal'));
        messageModal.show();
    }
});
// document.addEventListener('DOMContentLoaded', function () {
//     // Obtiene los mensajes desde el script de datos
//     var messagesData = document.getElementById('messages-data').textContent;
    
//     // Intenta analizar los mensajes JSON
//     var messages = [];
//     try {
//         messages = JSON.parse(messagesData || '[]');
//     } catch (e) {
//         console.error('Error parsing messages:', e);
//     }

//     // Filtra mensajes de error o advertencia
//     var errorMessages = messages.filter(msg => msg.level === 'error' || msg.level === 'warning');
    
//     // Verifica si hay mensajes de error o advertencia para mostrar
//     if (errorMessages.length > 0) {
//         var modalMessage = document.getElementById('modalMessage');
//         modalMessage.innerHTML = errorMessages.map(msg => `
//             <div class="alert alert-info">${msg}</div>
//         `).join('');
        
//         var messageModal = new bootstrap.Modal(document.getElementById('messageModal'));
//         messageModal.show();
//     }
// });
