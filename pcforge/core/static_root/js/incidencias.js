document.addEventListener('DOMContentLoaded', function () {
    const buttonsDelete = document.querySelectorAll('.delete-incidencias');

    const csrfToken = getCSRFToken();

    buttonsDelete.forEach((button) => {
        button.addEventListener('click', function () {
            const incidenciaId = parseInt(this.getAttribute('data-config-id'));
            console.log("id: ", incidenciaId);
            if (confirm('¿Estás seguro de que quieres eliminar esta incidencia?')) {
                fetch(`/api/eliminar_incidencia/${incidenciaId}`, {
                    method: 'DELETE',
                    headers: {
                        'X-CSRFToken': csrfToken
                    }
                })
                    .then(response => {
                        if (response.ok) {
                            location.reload();
                        } else {
                            throw new Error('Error al eliminar la incidencia.');
                        }
                    })
                    .catch(error => {
                        alert(error.message);
                    });
            }
        });
    });



    const openButtons = document.querySelectorAll('.open-quickview-btn');
    const closeButtons = document.querySelectorAll('.quickview');

    openButtons.forEach((button) => {
        button.addEventListener('click', () => {
            const configId = button.dataset.configId;
            const quickview = document.querySelector(`.quickview[data-config-id="${configId}"]`);

            if (quickview) {
                quickview.classList.toggle('hidden');
            }
        });
    });

    closeButtons.forEach((button) => {
        button.addEventListener('click', () => {
            const quickview = button.closest('.quickview');
            if (quickview) {
                quickview.classList.add('hidden');
            }
        });
    });

    function getCSRFToken() {
        let csrfToken = null;
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            const [name, value] = cookie.trim().split('=');
            if (name === 'csrftoken') {
                csrfToken = value;
                break;
            }
        }
        return csrfToken;
    }
});
