document.addEventListener('DOMContentLoaded', function () {
  const configuracionesList = document.getElementById('configuraciones-list');

  const csrfToken = getCSRFToken();

  fetch("/api/configuraciones_usuario")
    .then(response => response.json())
    .then(data => {
      configuracionesList.style.display = 'grid';
      configuracionesList.innerHTML = '';
      if (data.length === 0) {
        console.log('No hay configuraciones');

        const productElement = document.createElement('div');
        productElement.classList.add('bg-white');

        productElement.innerHTML = `
          <div class="border border-gray-500 rounded-3xl mx-auto grid max-w-2xl grid-cols-1 items-center gap-x-8 gap-y-16 px-4 py-24 sm:px-6 sm:py-32 lg:max-w-7xl lg:grid-cols-1 lg:px-8 text-center">
              <div class="text-center">
                  <h1 class="mt-4 text-2xl font-bold tracking-tight text-gray-900 sm:text-5xl">No has guardado configuraciones aún.</h1>
                  <p class="mt-6 text-base leading-7 text-gray-600">Comienza a crear tu PC perfecto.</p>
                  <div class="mt-10 flex items-center justify-center gap-x-6">
                      <a href="{% url 'ensamblador'%}" class="rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Volver</a>
                      <a href="{% url 'index' %}" class="text-sm font-semibold text-gray-900">Más información<span aria-hidden="true">&rarr;</span></a>
                  </div>
              </div>
          </div>
        `;
        configuracionesList.appendChild(productElement);
        return;
      } else {
        console.log('Configuraciones recibidas:', data);

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
            console.log('Detalles de componentes recibidos:', componentes);

            configuracionesList.style.display = 'grid';
            configuracionesList.innerHTML = '';

            data.forEach(item => {
              const producto = item.fields;
              const productoID = item.pk;
              const productElement = document.createElement('div');
              productElement.classList.add('bg-white');

              const chasisDetail = getComponentFactura(componentes.chasis, producto.chasis);
              const placaBaseDetail = getComponentFactura(componentes.placa_base, producto.placa_base);
              const cpuDetail = getComponentFactura(componentes.cpu, producto.cpu);
              const ramDetail = getComponentFactura(componentes.ram, producto.ram);
              const almacenamientoDetail = getComponentFactura(componentes.almacenamiento, producto.almacenamiento);
              const fuenteAlimentacionDetail = getComponentFactura(componentes.fuente_alimentacion, producto.fuente_alimentacion);
              const gpuDetail = getComponentFactura(componentes.gpu, producto.gpu);

              const configDetail = {
                chasis: chasisDetail,
                placa_base: placaBaseDetail,
                cpu: cpuDetail,
                ram: ramDetail,
                almacenamiento: almacenamientoDetail,
                fuente_alimentacion: fuenteAlimentacionDetail,
                gpu: gpuDetail,
                precio: producto.precio
              };

              const date = new Date(producto.fecha_creacion);

              const day = date.getDate();
              const month = date.getMonth() + 1;
              const year = date.getFullYear();
              const formattedDate = `${day}-${month}-${year}`;

	      const gpuDetail = getComponentDetail(componentes.gpu, producto.gpu);
              console.log('Producto:', JSON.stringify(producto))

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
                      <div class="border-t border-gray-400 pt-4">
                        <dt class="font-medium font-bold text-gray-900">Para asegurar la exactitud de los precios, le informamos que esta configuración fue realizada el ${formattedDate}. Por favor, tenga en cuenta que los precios podrían actualizarse después de esta fecha.</dt>
                      </div>
                  </section>
                  <section>
                    <button class="delete-config-btn rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600" data-config-id="${productoID}">Eliminar Configuración</button>
                    <button class="generate-pdf-btn rounded-md bg-green-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-green-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-green-600" data-config-id="${productoID}" data-config-detail='${JSON.stringify(configDetail)}'>Generar Factura PDF</button>
                  </section>
                </div>
              `;

              configuracionesList.appendChild(productElement);
            });
          })
          .catch(error => {
            console.error('Error al obtener detalles de componentes:', error);
          });
      }
    })
    .catch(error => {
      console.error('Error al obtener configuraciones:', error);
    });

  document.addEventListener('click', function (event) {
    if (event.target.classList.contains('delete-config-btn')) {
      const configId = parseInt(event.target.getAttribute('data-config-id'));
      console.log('La configID es', configId);
      deleteConfiguration(configId);
    } else if (event.target.classList.contains('generate-pdf-btn')) {
      const configDetail = JSON.parse(event.target.getAttribute('data-config-detail'));
      generatePDF(configDetail);
    }
  });

  function deleteConfiguration(configId) {
    const csrfToken = getCSRFToken();
    const payload = JSON.stringify({ config_id: configId });

    fetch('/api/delete_configuration', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: payload
    })
      .then(response => {
        if (response.ok) {
          console.log('Configuración eliminada con éxito');
          alert('Configuración eliminada con éxito');
          location.reload();
        } else {
          console.error('Error al eliminada la configuración');
          alert('Error al eliminada la configuración');
        }
      })
      .catch(error => {
        console.error('Error al hacer la petición de guardar configuración:', error);
        alert('Error al hacer la petición de guardar configuración');
      });
  }

  function generatePDF(configDetail) {
    console.log('ConfigDetail:', configDetail);
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    const fontRegular = 'Helvetica';
    const fontBold = 'Helvetica-Bold';

    const empresaNombre = "PCForge y Multimedia SLU";
    const empresaDireccion = "Avda Rúa Antonio, 2, Pol.Ind. La Palmera";
    const empresaDireccion2 = "04009. El Ejido. Almería. España";
    const empresaTelefono = "601 103 734";
    const empresaEmail = "pcforge@email.com";

    const fecha = new Date().toLocaleDateString();

    doc.setFontSize(11);
    doc.setFont(fontRegular);
    doc.text(empresaNombre, 148.7, 15);
    doc.text(empresaDireccion, 123.5, 20);
    doc.text(empresaDireccion2, 138.5, 25);
    doc.text(empresaEmail, 160.5, 30);
    doc.text(empresaTelefono, 173.5, 35);
    doc.text(fecha, 180, 40);

    doc.setFontSize(20);
    doc.setFont(fontBold);
    doc.text('PCForge', 45, 22);

    doc.setDrawColor(200);
    doc.setLineWidth(0.5);
    doc.line(15, 45, 195, 45);

    doc.setFont(fontRegular);
    const svgString = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 47 40" fill="none"><path fill="#6366f1" d="M23.5 6.5C17.5 6.5 13.75 9.5 12.25 15.5C14.5 12.5 17.125 11.375 20.125 12.125C21.8367 12.5529 23.0601 13.7947 24.4142 15.1692C26.6202 17.4084 29.1734 20 34.75 20C40.75 20 44.5 17 46 11C43.75 14 41.125 15.125 38.125 14.375C36.4133 13.9471 35.1899 12.7053 33.8357 11.3308C31.6297 9.09158 29.0766 6.5 23.5 6.5ZM12.25 20C6.25 20 2.5 23 1 29C3.25 26 5.875 24.875 8.875 25.625C10.5867 26.0529 11.8101 27.2947 13.1642 28.6693C15.3702 30.9084 17.9234 33.5 23.5 33.5C29.5 33.5 33.25 30.5 34.75 24.5C32.5 27.5 29.875 28.625 26.875 27.875C25.1633 27.4471 23.9399 26.2053 22.5858 24.8307C20.3798 22.5916 17.8266 20 12.25 20Z"/></svg>';
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    const DOMURL = window.URL || window.webkitURL || window;
    const img = new Image();
    const svgBlob = new Blob([svgString], { type: 'image/svg+xml;charset=utf-8' });
    const url = DOMURL.createObjectURL(svgBlob);

    img.onload = function () {
      canvas.width = img.width;
      canvas.height = img.height;
      context.drawImage(img, 0, 0);

      const pngData = canvas.toDataURL('image/png');
      const imgData = pngData.substring(pngData.indexOf(',') + 1);

      doc.addImage(imgData, 'PNG', 15, 5, 30, 30);
      DOMURL.revokeObjectURL(pngData);

      doc.setFontSize(30);
      doc.text("PRESUPUESTO", 105, 60, null, null, 'center');

      const tableColumn = ["Componentes", "Modelo", "Vendedor", "Precio"];
      const tableRows = [];

      const components = [
        { name: "Chasis", detail: configDetail.chasis },
        { name: "Placa Base", detail: configDetail.placa_base },
        { name: "CPU", detail: configDetail.cpu },
        { name: "RAM", detail: configDetail.ram },
        { name: "Almacenamiento", detail: configDetail.almacenamiento },
        { name: "Fuente de Alimentación", detail: configDetail.fuente_alimentacion },
        { name: "GPU", detail: configDetail.gpu },
      ];

      components.forEach(component => {
        const componentData = [
          component.name,
          component.detail.modelName,
          component.detail.vendorName,
          `${component.detail.price} €`
        ];
        tableRows.push(componentData);
      });

      const TotalPrice = [
        "Total",
        "",
        "",
        `${configDetail.precio} €`,
      ];
      tableRows.push(TotalPrice);

      doc.autoTable(tableColumn, tableRows, { startY: 70 });

      doc.save('factura.pdf');
    };

    img.src = url;
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

  function getComponentFactura(componentArray, id) {
    const component = componentArray.find(item => item.id === id);
    if (component) {
      const modelName = component.modelo || 'Desconocido';
      const vendorName = component.vendedor || 'Desconocido';
      const price = component.precio || 'Desconocido';
      return { modelName, vendorName, price };
    } else {
      return { modelName: 'Desconocido', vendorName: 'Desconocido', price: 'Desconocido' };
    }
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
});
