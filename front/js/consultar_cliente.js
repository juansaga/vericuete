async function loadClients(nombre, estado) {

    // aqui se debería estraer los parametros d la función

    const response = await fetch(`http://127.0.0.1:8000/clientes/?cliente_nombre=${nombre}&estado=${estado}`, {
        method: 'GET'
    });
    const clients = await response.json();

    const info_cliente = [clients.clienteid, clients.nombre, clients.telefono]

    const ordenes = clients.ordenes

    const clientsList = document.getElementById('clients');
    clientsList.innerHTML = ''; // Limpiar la lista actual

    const listItem = document.createElement('li');
    listItem.textContent = `${info_cliente}`;
    clientsList.appendChild(listItem);

    for (const orden of ordenes) {
        const listItem = document.createElement('li');
        listItem.textContent = `${orden.ordenid} ${orden.fechaorden} ${orden.totalprendas} ${orden.estado} ${orden.pago}`;
        // Aquí puedes añadir más datos o incluso botones para editar/borrar

        clientsList.appendChild(listItem);
    }
}
loadClients('Juan Manuel', 'Recibido')