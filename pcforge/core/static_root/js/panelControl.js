document.addEventListener('DOMContentLoaded', function () {
    const estadisticasGenerales = document.getElementById('estadisticas-generales');
    const csrfToken = getCSRFToken();

    fetch('/api/stats', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log('ofi:', data['ofimatica'])
        sumaUso = data['ofimatica'] + data['gaming'] + data['ia'] + data['edicion'];
        sumaRend = data['gama_baja'] + data['gama_media'] + data['gama_alta'];


        const datos1 = [
            { nombre: 'Ofimática', porcentaje: ((data['ofimatica'] / sumaUso) * 100).toFixed(1) },
            { nombre: 'Gaming', porcentaje: ((data['gaming'] / sumaUso) * 100).toFixed(1) },
            { nombre: 'IA', porcentaje: ((data['ia'] / sumaUso) * 100).toFixed(1) },
            { nombre: 'Edición', porcentaje: ((data['edicion'] / sumaUso) * 100).toFixed(1) },
        ];
        
        const datos2 = [
            { nombre: 'Rendimiento básico', porcentaje: ((data['gama_baja'] / sumaRend) * 100).toFixed(1) },
            { nombre: 'Rendimiento equilibrado', porcentaje: ((data['gama_media'] / sumaRend) * 100).toFixed(1) },
            { nombre: 'Rendimiento alto', porcentaje: ((data['gama_alta'] / sumaRend) * 100).toFixed(1) },
        ];
        
    
        generarGrafico('grafico1', datos1);
        generarGrafico('grafico2', datos2);

        estadisticasGenerales.innerHTML = '';
        estadisticasGenerales.innerHTML = `
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-6">
            <div class="bg-white rounded-lg border border-gray-300 p-6 shadow-md text-center">
                <div class="mb-6">
                    <div class="text-2xl font-bold">Visitas de la página</div>
                    <div class="mt-1">
                        <div class="text-2xl">${data['visitas']}</div>
                    </div>
                </div>
            </div>
            <div class="bg-white rounded-lg border border-gray-300 p-6 shadow-md text-center">
                <div class="mb-6">
                    <div class="text-2xl font-bold">Usuarios registrados</div>
                    <div class="mt-1">
                        <div class="text-2xl">${data['usuarios']}</div>
                    </div>
                </div>
            </div>
            <div class="bg-white rounded-lg border border-gray-300 p-6 shadow-md text-center">
                <div class="mb-4">
                    <div class="text-2xl font-bold">Configuraciones creadas en BD</div>
                    <div class="mt-1">
                        <div class="text-2xl">${data['pcs']}</div>
                    </div>
                </div>
            </div>
            <div class="bg-white rounded-lg border border-gray-300 p-6 shadow-md text-center">
                <div class="mb-6">
                    <div class="text-2xl font-bold">Peticiones de asistencia</div>
                    <div class="text-2xl">${data['peticiones']}</div>
                </div>
            </div>
            <div class="bg-white rounded-lg border border-gray-300 p-6 shadow-md text-center">
                <div class="mb-6">
                    <div class="text-2xl font-bold">Configuraciones Guardadas</div>
                    <div class="text-2xl">${data['guardadas']}</div>
                </div>
            </div>
            <div class="bg-white rounded-lg border border-gray-300 p-6 shadow-md text-center">
                <div class="mb-6">
                    <div class="text-2xl font-bold">Incidencias activas</div>
                    <div class="text-2xl">${data['incidencias']}</div>
                </div>
            </div>
        </div>
          
            `;     

    })

    function mostrarSpinner() {
        const spinner = document.createElement('div');
        spinner.className = 'spinner fixed top-0 left-0 w-screen h-screen flex justify-center items-center bg-gray-900 bg-opacity-50 z-50';
        spinner.innerHTML = `
        <svg class="animate-spin h-10 w-10 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A8.001 8.001 0 014.735 4.734L2.343 7.127l1.414 1.414 2.342-2.342a6 6 0 108.486 8.486l-2.342 2.342 1.414 1.414 2.342-2.342A8.001 8.001 0 016 17.291z"></path>
        </svg>
    `;
        // Añade el spinner al body
        document.body.appendChild(spinner);
    }

    function llamarAPI(endpoint, method) {
        const csrfToken = getCSRFToken();
        console.log('Llamando al endpoint:', endpoint);
        fetch(endpoint, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
        })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Error en la respuesta de la API');
                }
            })
            .catch(error => {
                console.error('Error en la llamada a la API:', error);
            })
            .finally(() => {
                ocultarSpinner();
            });
    }

    function ocultarSpinner() {
        const spinner = document.querySelector('.spinner');
        if (spinner) {
            spinner.remove();
        }
    }


    // Función principal para manejar el click en los botones
    function manejarClick(event) {
        event.preventDefault();
        const buttonId = event.target.id;
        mostrarSpinner();
        switch (buttonId) {
            case 'webScrapingButton':
                llamarAPI('/api/webscraping', 'GET');
                break;
            case 'actualizarBDButton':
                llamarAPI('/api/rellenarBD', 'PUT');
                break;
            case 'crearPCsButton':
                llamarAPI('/api/crearPCs/', 'PUT');
                break;
            default:
                console.log('Botón no reconocido');
        }
    }

    const crearPCsButton = document.getElementById("crearPCsButton");
    crearPCsButton.addEventListener("click", manejarClick);    

    const webScrapingButton = document.getElementById("webScrapingButton");
    webScrapingButton.addEventListener("click", manejarClick); 


    const actualizarBDButton = document.getElementById("actualizarBDButton");
    actualizarBDButton.addEventListener("click", manejarClick); 

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

    
    function generarGrafico(idContenedor, datos) {
        const grafico = document.getElementById(idContenedor);
        grafico.innerHTML = ''; // Limpiar el contenido existente
    
        datos.forEach(dato => {
            const barraContenedor = document.createElement('div');
            barraContenedor.className = 'grid grid-cols-2 items-center mb-1';
            
            const nombre = document.createElement('div');
            nombre.textContent = dato.nombre;
            barraContenedor.appendChild(nombre);
    
            const barra = document.createElement('div');
            barra.className = 'rounded-md text-white text-xs font-semibold text-center p-1';
            barra.style.backgroundColor = 'rgb(216, 216, 216)'; // Color de fondo gris claro
            barraContenedor.appendChild(barra);
    
            const porcentaje = document.createElement('div');
            porcentaje.className = 'bg-indigo-500 rounded rounded-md text-white text-xs font-semibold text-center p-1';
            porcentaje.style.width = `${dato.porcentaje}%`;
            porcentaje.textContent = `${dato.porcentaje}%`;
            barra.appendChild(porcentaje);
    
            grafico.appendChild(barraContenedor);
        });
    }
    
    
    



});
