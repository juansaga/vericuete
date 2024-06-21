document.getElementById('order_search_form').addEventListener('submit', async (e) => {
    e.preventDefault();

    // Extracción de parámetros
    const orden = document.getElementById('order_search_input').value;
    const response = await fetch(`http://127.0.0.1:8000/ordenes/?orden_id=${orden}`, {
        method: 'GET'
    });

    const ordenes = await response.json();

    const detalle_ordenes = [ordenes.ordenid, ordenes.clienteid, ordenes.fechaorden, ordenes.totalprendas,ordenes.estado, ordenes.pago]
})

