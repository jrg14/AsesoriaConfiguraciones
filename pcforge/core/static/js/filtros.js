document.addEventListener('DOMContentLoaded', function () {
    const initialFilters = document.getElementById('initial-filters');
    const subFilters = document.getElementById('sub-filters');
    const priceFilter = document.getElementById('price-filter');
    const productList = document.getElementById('product-list');
    const loadingSpinner = document.getElementById('loading-spinner');
    const sinConfiguraciones = document.getElementById('sinComponentes')
    let selectedInitialFilter = null;
    let selectedSubFilter = null;

    initialFilters.addEventListener('click', function (event) {
        const filterClicked = event.target.closest('.filter-container');
        if (filterClicked) {
            selectedInitialFilter = filterClicked.getAttribute('data-filter');
            initialFilters.style.display = 'none';
            subFilters.style.display = 'inherit';
        }
    });

    subFilters.addEventListener('click', function (event) {
        const subFilterClicked = event.target.closest('.filter-container');
        if (subFilterClicked && selectedInitialFilter) {
            selectedSubFilter = subFilterClicked.getAttribute('data-filter');
            subFilters.style.display = 'none';
            priceFilter.style.display = 'inherit';
        }
    });

    document.getElementById('price-min').addEventListener('input', function () {
        document.getElementById('price-min-value').textContent = this.value + ' €';
    });

    document.getElementById('price-max').addEventListener('input', function () {
        document.getElementById('price-max-value').textContent = this.value + ' €';
    });

    document.getElementById('apply-price-filter').addEventListener('click', function () {
        const selectedPriceMin = document.getElementById('price-min').value;
        const selectedPriceMax = document.getElementById('price-max').value;
        const combinedFilter = `${selectedInitialFilter}_${selectedSubFilter}`;

        if (parseInt(selectedPriceMin) > parseInt(selectedPriceMax)) {
            alert('El precio mínimo no puede ser mayor que el precio máximo.');
            return;
        }

        const csrfToken = getCSRFToken();
        mostrarSpinner();

        console.log('Filtro combinado seleccionado:', combinedFilter);
        console.log('Precio min seleccionado:', selectedPriceMin);
        console.log('Precio max seleccionado:', selectedPriceMax);


        fetch(`/api/filtrar?filtro=${combinedFilter}&precio_min=${selectedPriceMin}&precio_max=${selectedPriceMax}`)
            .then(response => response.json())
            .then(data => {
                if (data.length === 0) {
                    priceFilter.style.display = 'none';
                    productList.style.display = 'none';
                    sinConfiguraciones.style.display = 'inherit';
                    ocultarSpinner();
                    return;
                } else {
                    const ids = [...new Set(data.flatMap(item => [
                        item.fields.chasis,
                        item.fields.placa_base,
                        item.fields.cpu,
                        item.fields.ram,
                        item.fields.almacenamiento,
                        item.fields.fuente_alimentacion,
                        item.fields.gpu
                    ]))];

                    return fetch('/api/componentes/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': csrfToken
                        },
                        body: JSON.stringify({ ids })
                    })
                        .then(response => response.json())
                        .then(componentes => {
                            priceFilter.style.display = 'none';
                            productList.style.display = 'grid';
                            productList.innerHTML = '';

                            // Mapeamos cada configuración a una promesa de fetch
                            const chatPromises = data.map((item, index) => {
                                const producto = item.fields;
                                const productoID = item.pk;

                                const prompt = `Hola, ChatGPT. Tengo una lista de componentes de ordenador que estoy considerando para armar una nueva PC. 
                                Dime lo bueno de este pc para un uso de ${selectedInitialFilter} siendo de ${selectedSubFilter} sin nombrar el modelo del componentes, en forma de texto narrativo lo más escueto 
                                posible (3-5 lineas). Aquí está la lista: 
                                Chasis: ${getComponentModel(componentes.chasis, producto.chasis)}, 
                                Placa Base: ${getComponentModel(componentes.placa_base, producto.placa_base)}, 
                                CPU: ${getComponentModel(componentes.cpu, producto.cpu)}, 
                                RAM: ${getComponentModel(componentes.ram, producto.ram)}, 
                                Almacenamiento: ${getComponentModel(componentes.almacenamiento, producto.almacenamiento)}, 
                                Fuente de Alimentación: ${getComponentModel(componentes.fuente_alimentacion, producto.fuente_alimentacion)}, 
                                GPU: ${getComponentModel(componentes.gpu, producto.gpu)}.`;

                                return fetch('/api/chatgpt', {
                                    method: 'POST',
                                    headers: {
                                        'Content-Type': 'application/json',
                                        'X-CSRFToken': csrfToken
                                    },
                                    body: JSON.stringify({ prompt })
                                })
                                    .then(response => response.json())
                                    .then(chatResponse => {
                                        return { producto, productoID, chatResponse, index };
                                    });
                            });

                            // Esperamos a que todas las promesas se resuelvan
                            return Promise.all(chatPromises)
                                .then(results => {
                                    results.sort((a, b) => a.index - b.index); // Ordenamos los resultados por el índice original
                                    results.forEach(({ producto, productoID, chatResponse }) => {
                                        const date = new Date(producto.fecha_creacion);

                                        const day = date.getDate();
                                        const month = date.getMonth() + 1;
                                        const year = date.getFullYear();
                                        const formattedDate = `${day}-${month}-${year}`;
                                        const productElement = document.createElement('div');
                                        productElement.classList.add('bg-white');
                                        const gpuDetail = getComponentDetail(componentes.gpu, producto.gpu);
                                        productElement.innerHTML = `
                                            <div class="border border-gray-500 rounded-3xl mx-auto grid max-w-2xl grid-cols-1 items-center gap-x-8 gap-y-16 px-4 py-24 sm:px-6 sm:py-32 lg:max-w-7xl lg:grid-cols-1 lg:px-8 text-center">
                                            <section>
                                                <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Especificaciones técnicas</h2>
                                                <dl class="mt-16 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-4 sm:gap-y-16 lg:gap-x-8">
                                                    <div class="border-t border-gray-400 pt-4">
                                                        <dt class="font-medium font-bold text-gray-900">Chasis</dt>
                                                        <dd class="mt-2 text-sm text-gray-700 min-h-[40px]">${getComponentDetail(componentes.chasis, producto.chasis)}</dd>
                                                    </div>
                                                    <div class="border-t border-gray-400 pt-4">
                                                        <dt class="font-medium font-bold text-gray-900">Placa Base</dt>
                                                        <dd class="mt-2 text-sm text-gray-700 min-h-[40px]">${getComponentDetail(componentes.placa_base, producto.placa_base)}</dd>
                                                    </div>
                                                    <div class="border-t border-gray-400 pt-4">
                                                        <dt class="font-medium font-bold text-gray-900">CPU</dt>
                                                        <dd class="mt-2 text-sm text-gray-700 min-h-[40px]">${getComponentDetail(componentes.cpu, producto.cpu)}</dd>
                                                    </div>
                                                    <div class="border-t border-gray-400 pt-4">
                                                        <dt class="font-medium font-bold text-gray-900">RAM</dt>
                                                        <dd class="mt-2 text-sm text-gray-700 min-h-[40px]">${getComponentDetail(componentes.ram, producto.ram)}</dd>
                                                    </div>
                                                    <div class="border-t border-gray-400 pt-4">
                                                        <dt class="font-medium font-bold text-gray-900">Almacenamiento</dt>
                                                        <dd class="mt-2 text-sm text-gray-700 min-h-[40px]">${getComponentDetail(componentes.almacenamiento, producto.almacenamiento)}</dd>
                                                    </div>
                                                    <div class="border-t border-gray-400 pt-4">
                                                        <dt class="font-medium font-bold text-gray-900">Fuente de Alimentación</dt>
                                                        <dd class="mt-2 text-sm text-gray-700 min-h-[40px]">${getComponentDetail(componentes.fuente_alimentacion, producto.fuente_alimentacion)}</dd>
                                                    </div>
                                                    <div class="border-t border-gray-400 pt-4">
                                                        <dt class="font-medium font-bold text-gray-900">GPU</dt>
                                                        <dd class="mt-2 text-sm text-gray-700 min-h-[40px]">${gpuDetail === 'Desconocido' ? 'Sin GPU': gpuDetail}</dd>
                                                    </div>
                                                    <div class="border-t border-gray-400 pt-4">
                                                        <dt class="font-medium font-bold text-gray-900">Precio</dt>
                                                        <dd class="mt-2 text-sm text-gray-700 min-h-[40px]">${producto.precio} €</dd>
                                                    </div>
                                                </dl>
                                            </section>
                                            <section>
                                                <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Descripción</h2>
                                                <p class="mt-4 text-gray-700">${chatResponse.message}</p>
                                            </section>
                                            <section>
                                                <div class="border-t border-gray-400 pt-4">
                                                    <dt class="font-medium font-bold text-gray-900">Para asegurar la exactitud de los precios, le informamos que esta configuración fue realizada el ${formattedDate}. Por favor, tenga en cuenta que los precios podrían actualizarse después de esta fecha.</dt>
                                                </div>
                                            </section>
                                            <section>
                                                <button class="save-config-btn rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600" data-config-id="${productoID}">Guardar Configuración</button>
                                            </section>
                                            </div>
                                        `;
                                        productList.appendChild(productElement);
                                    });
                                })
                                .catch(error => {
                                    console.error('Error al obtener la respuesta de ChatGPT:', error);
                                })
                                .finally(() => {
                                    ocultarSpinner();
                                });
                        });
                }
            })
            
            .catch(error => {
                console.error('Error al filtrar productos:', error);
                ocultarSpinner();
            });
    });

    document.addEventListener('click', function (event) {
        if (event.target.classList.contains('save-config-btn')) {
            const configId = parseInt(event.target.getAttribute('data-config-id'));
            console.log('La configID es', configId)
            saveConfiguration(configId);
        }
    });
    function saveConfiguration(configId) {
        const csrfToken = getCSRFToken();

        const payload = JSON.stringify({ config_id: configId });

        fetch('/api/save_configuration', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: payload
        })
            .then(response => {
                if (response.ok) {
                    console.log('Configuración guardada con éxito');
                    alert('Configuración guardada con éxito');
                } else {
                    console.error('Error al guardar la configuración');
                    alert('Error al guardar la configuración: Tienes que haber iniciado sesión');
                }
            })
            .catch(error => {
                console.error('Error al hacer la petición de guardar configuración:', error);
                alert('Error al hacer la petición de guardar configuración');
            });
    }


    function getComponentDetail(componentArray, id) {
        const component = componentArray.find(item => item.id === id);
        if (component) {
            const modelName = component.modelo || 'Desconocido';
            const vendorName = component.vendedor || 'Desconocido';
            return `${modelName} - ${vendorName}`;
        } else {
            return 'Desconocido';
        }
    }

    function getComponentModel(componentArray, id) {
        const component = componentArray.find(item => item.id === id);
        if (component) {
            const modelName = component.modelo;
            return `${modelName}`;
        } else {
            return 'Desconocido';
        }
    }

    function getComponentModel(componentArray, id) {
        const component = componentArray.find(item => item.id === id);
        return component ? component.modelo || 'Desconocido' : 'Desconocido';
    }

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

    function mostrarSpinner() {
        const spinner = document.createElement('div');
        spinner.className = 'spinner fixed top-0 left-0 w-screen h-screen flex justify-center items-center bg-gray-900 bg-opacity-50 z-50';
        spinner.innerHTML = `
            <svg class="animate-spin h-10 w-10 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A8.001 8.001 0 014.735 4.734L2.343 7.127l1.414 1.414 2.342-2.342a6 6 0 108.486 8.486l-2.342 2.342 1.414 1.414 2.342-2.342A8.001 8.001 0 016 17.291z"></path>
            </svg>
        `;
        document.body.appendChild(spinner);
    }

    function ocultarSpinner() {
        const spinner = document.querySelector('.spinner');
        if (spinner) {
            spinner.remove();
        }
    }
});
