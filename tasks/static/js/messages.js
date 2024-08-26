document.addEventListener('DOMContentLoaded', function () {
    var messagesData = document.getElementById('messages-data').textContent;
    var messages = JSON.parse(messagesData || '[]');
    if (messages.length > 0) {
        var modalMessage = document.getElementById('modalMessage');
        modalMessage.innerHTML = messages.map(msg => `
            <div class="alert alert-info">${msg}</div>
        `).join('');
        var messageModal = new bootstrap.Modal(document.getElementById('messageModal'));
        messageModal.show();
    }
});