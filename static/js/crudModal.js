function openModal(idmodal) {
    const elementModal = '#' + idmodal + '.space_modal';
    const overlay = document.getElementById('overlayModal');
    const enlargedModal = document.getElementById('enlargedModal');
    const modalDiv = document.querySelector(elementModal);

    enlargedModal.innerHTML = modalDiv.outerHTML;
    const modalClonado = enlargedModal.querySelector(elementModal);

    modalClonado.style.display = 'flex';
    overlay.style.display = 'flex';

    llenarSelectsDelModal(modalClonado);

    const mapContainer = modalClonado.querySelector('.map_space[data-has-map]');
    if (mapContainer) {
        const uniqueMapId = 'map_' + Date.now();
        const mapDiv = document.createElement('div');
        mapDiv.id = uniqueMapId;
        mapDiv.style.height = '250px';
        mapDiv.style.width = '400px';
        mapContainer.appendChild(mapDiv);

        // Obtener inputs ANTES de crear el mapa
        const direccionInput = modalClonado.querySelector('#direccion');
        const latitudInput = modalClonado.querySelector('#latitud');
        const longitudInput = modalClonado.querySelector('#longitud');
        const codigoPostalInput = modalClonado.querySelector('#codigo_postal');

        let currentMarker = null;

        // Coordenadas guardadas
        let initialLat = -9.1900;
        let initialLng = -75.0152;
        let initialZoom = 5;

        const latSaved = parseFloat(latitudInput?.value);
        const lngSaved = parseFloat(longitudInput?.value);

        if (!isNaN(latSaved) && !isNaN(lngSaved)) {
            initialLat = latSaved;
            initialLng = lngSaved;
            initialZoom = 16;
        }

        const map = L.map(uniqueMapId).setView([initialLat, initialLng], initialZoom);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap contributors'
        }).addTo(map);

        function reverseGeocode(lat, lng) {
            const url = `https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${lat}&lon=${lng}&addressdetails=1`;

            fetch(url)
                .then(response => response.json())
                .then(data => {
                    if (direccionInput) direccionInput.value = data.display_name || '';
                    if (latitudInput) latitudInput.value = lat.toFixed(6);
                    if (longitudInput) longitudInput.value = lng.toFixed(6);

                    const address = data.address || {};
                    if (codigoPostalInput) codigoPostalInput.value = address.postcode || '';
                })
                .catch(() => {
                    if (direccionInput) direccionInput.value = 'Error al obtener dirección';
                    if (latitudInput) latitudInput.value = lat.toFixed(6);
                    if (longitudInput) longitudInput.value = lng.toFixed(6);
                });
        }

        // Mostrar marcador si ya hay coordenadas guardadas
        if (!isNaN(latSaved) && !isNaN(lngSaved)) {
    currentMarker = L.marker([latSaved, lngSaved]).addTo(map);
    currentMarker.bindPopup(`
        <div style="text-align: center;">
            <strong>Ubicación Guardada</strong><br>
            <small>Lat: ${latSaved.toFixed(6)}<br>Lng: ${lngSaved.toFixed(6)}</small>
        </div>
    `).openPopup();

    // Solo hacer reverseGeocode si direccion o codigo postal están vacíos
    const direccionVacia = !direccionInput?.value?.trim();
    const postalVacio = !codigoPostalInput?.value?.trim();
    if (direccionVacia || postalVacio) {
        reverseGeocode(latSaved, lngSaved);
    }
}


        // Al hacer clic en el mapa
        map.on('click', function (e) {
            const { lat, lng } = e.latlng;

            if (currentMarker) map.removeLayer(currentMarker);
            currentMarker = L.marker([lat, lng]).addTo(map);
            currentMarker.bindPopup(`
                <div style="text-align: center;">
                    <strong>Ubicación Seleccionada</strong><br>
                    <small>Lat: ${lat.toFixed(6)}<br>Lng: ${lng.toFixed(6)}</small>
                </div>
            `).openPopup();

            reverseGeocode(lat, lng);
        });

        map.getContainer().style.cursor = 'crosshair';

        // Buscador de direcciones
        L.Control.geocoder({
            defaultMarkGeocode: false,
            placeholder: 'Buscar dirección...',
            errorMessage: 'No se encontró el lugar',
            geocoder: L.Control.Geocoder.nominatim({ geocodingQueryParams: { countrycodes: 'pe' } })
        })
            .on('markgeocode', function (e) {
                const latlng = e.geocode.center;
                map.setView(latlng, 16);

                if (currentMarker) map.removeLayer(currentMarker);
                currentMarker = L.marker(latlng).addTo(map);
                currentMarker.bindPopup(`
                    <div style="text-align: center;">
                        <strong>Resultado de Búsqueda</strong><br>
                        <small>Lat: ${latlng.lat.toFixed(6)}<br>Lng: ${latlng.lng.toFixed(6)}</small>
                    </div>
                `).openPopup();

                reverseGeocode(latlng.lat, latlng.lng);
            })
            .addTo(map);
    }
}


function closeModal() {
    const overlay = document.getElementById('overlayModal');
    const enlargedModal = document.getElementById('enlargedModal');

    // Limpiar selects antes de cerrar (por si queda en memoria)
    const modalAbierto = enlargedModal.querySelector('.space_modal');
    if (modalAbierto) {
        limpiarSelectsDelModal(modalAbierto);
    }

    overlay.style.display = 'none';
    enlargedModal.innerHTML = ''; // Limpiar modal para evitar acumulación de nodos
}

document.querySelectorAll('.clickable-modal').forEach(button => {
    button.addEventListener('click', function (event) {
        openModal(button.id);
    });
});


const divs = document.querySelectorAll('.td_content:not(.td_primary_key)');

divs.forEach(div => {
    let elementP = div.querySelector('.p_value');
    if (elementP) {
        let content = elementP.innerText.trim();

        if (!isNaN(content) && content.includes('.')) {
            div.classList.add('td_right');
        }
        else if (!isNaN(content)) {
            div.classList.add('td_right');
        }
        else {
            div.classList.add('td_left');
        }
    }
});


document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelectorAll(".form_fields");
    forms.forEach(form => {
        const inputs = form.querySelectorAll(".form_field:not(.form_textarea)");
        const cantidad = inputs.length;

        let columnas = 1;
        if (cantidad <= 2) columnas = cantidad;
        else if (cantidad === 4) columnas = 2;
        else columnas = 3;

        form.style.gridTemplateColumns = `repeat(${columnas}, 1fr)`;

    });

});




function llenarSelectsDelModal(modal) {
    const selects = modal.querySelectorAll("select[data-select]");
    selects.forEach(select => {
        const key = select.dataset.select;
        const opciones = SELECT_OPTIONS[key] || [];

        // Si ya está lleno, no lo volvemos a llenar
        if (select.options.length > 1) return;

        opciones.forEach(op => {
            const option = document.createElement("option");
            option.value = op.value;
            option.textContent = op.label;

            const valorSeleccionado = select.getAttribute("data-select-value");
            if (valorSeleccionado !== null && valorSeleccionado == op.value) {
                option.selected = true;
            }

            select.appendChild(option);
        });

        // Si es modo insert y no hay valor, selecciona el placeholder
        if (select.dataset.modo === "insert") {
            select.value = "-1";
        }
    });
}

function limpiarSelectsDelModal(modal) {
    const selects = modal.querySelectorAll("select[data-select]");
    selects.forEach(select => {
        select.innerHTML = ""; // Limpia todo
    });
}




document.addEventListener('input', (e) => {
    if (e.target.matches('.form_icon input[type="text"]:not(:disabled)')) {
        const input = e.target;
        const block_icon = input.closest('.form_icon').querySelector('i');

        const valor = input.value.trim();
        const claseIcono = valor.split(' ').find(clase => clase.startsWith('fa-') && clase !== 'fa-solid');
        if (claseIcono && block_icon) {
            block_icon.className = `fa-solid ${claseIcono}`;
        }
    }
});


document.addEventListener('input', (e) => {
    if (e.target.matches('.input_color_sync')) {
        const input = e.target;
        const name = input.dataset.name;
        const value = input.value;

        // Buscar los otros inputs con el mismo data-name, pero que no sean el que disparó el evento
        const siblings = document.querySelectorAll(`.input_color_sync[data-name="${name}"]`);
        siblings.forEach(el => {
            if (el !== input) {
                el.value = value;
            }
        });
    }
});


document.addEventListener('change', (e) => {
    if (e.target.matches('.form_img input[type="file"]:not(:disabled)')) {
        const input = e.target;
        const imgPrev = input.closest('.form_img').querySelector('img');

        if (e.target.files && e.target.files[0]) {
            const reader = new FileReader();
            reader.onload = function (event) {
                imgPrev.src = event.target.result;
            }
            reader.readAsDataURL(e.target.files[0]);
        }
    }
});








