async function loadClients() {
    const response = await fetch('http://127.0.0.1:8000/clientes/', {
        method: 'GET'
    });
    const clients = await response.json();

    const clientsList = document.getElementById('clients');
    clientsList.innerHTML = ''; // Limpiar la lista actual

    for (const client of clients) {
        const listItem = document.createElement('li');
        listItem.textContent = `${client.clienteid} ${client.nombre} ${client.apellido} ${client.telefono}`;
        // Aquí puedes añadir más datos o incluso botones para editar/borrar

        clientsList.appendChild(listItem);
    }
}
loadClients()