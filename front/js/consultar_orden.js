document.getElementById('order_search_form').addEventListener('submit', async (e) => {
    e.preventDefault();

    // Extracción de parámetros
    const estado = document.getElementById('order_search_input').value;
    const response = await fetch(`http://127.0.0.1:8000/orden/?estado=${estado}`, {
        method: 'GET'
    });

    const ordenes = await response.json();

    // const detalle_ordenes = [ordenes.ordenid, ordenes.clienteid, ordenes.fechaorden, ordenes.totalprendas,ordenes.estado, ordenes.pago]
    let ordenList = document.getElementById('ordenes')

    for (const orden of ordenes) {
        const listItem = document.createElement('li');
        listItem.textContent = `${orden.ordenid} ${orden.clienteid} ${orden.fechaorden} ${orden.totalprendas} ${orden.estado} ${orden.pago}`;
        // Aquí puedes añadir más datos o incluso botones para editar/borrar

        ordenList.appendChild(listItem);
    }
})

