document.getElementById('add-client-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const apellido = document.getElementById('apellido').value;
    const telefono = document.getElementById('telefono').value;
    // Agrega más campos según sea necesario

    try {
        const response = await fetch('http://127.0.0.1:8000/clientes/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ nombre, apellido, telefono /* Agrega más campos aquí */ }),
        });

        if (response.ok) {
            console.log('Cliente agregado exitosamente');
            loadClients(); // Recargar la lista de clientes después de agregar
        } else {
            console.error('Error al agregar cliente');
        }
    } catch (error) {
        console.error('Error:', error);
    }
});

async function loadClients() {
    const response = await fetch('http://127.0.0.1:8000/clientes/', {
        method: 'GET'
    });
    const clients = await response.json();

    const clientsList = document.getElementById('clients');
    clientsList.innerHTML = ''; // Limpiar la lista actual

    for (const client of clients) {
        const listItem = document.createElement('li');
        listItem.textContent = `${client.clienteId} ${client.nombre} ${client.apellido} ${client.telefono}`;
        // Aquí puedes añadir más datos o incluso botones para editar/borrar

        clientsList.appendChild(listItem);
    }
}

// Llamar a loadClients al cargar la página para mostrar la lista de clientes existentes
document.addEventListener('DOMContentLoaded', () => {
    loadClients();
});



// Suponiendo que el resto del script para manejar clientes ya está definido...

document.getElementById('add-order-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    // Obtén los valores de los campos del formulario
    const clienteId = document.getElementById('clienteId').value;
    const totalprendas = document.getElementById('totalprendas').value;
    const estado = document.getElementById('estado').value;
    const pago = document.getElementById('pago').value;
    const now = new Date();
    const fecha = now.toISOString().slice(0, 19).replace('T', ' ');
    // Asumiendo que tienes otros campos como fechaOrden, etc., añádelos aquí

    // Construye el objeto con los datos recogidos
    const orderData = {
        clienteId: clienteId,
        fechaorden: fecha,
        totalprendas: totalprendas,
        estado: estado,
        pago: pago
        // Añade otros campos aquí según tu modelo de datos
    };

    try {
        // Realiza la petición POST para crear la nueva orden
        const response = await fetch('http://127.0.0.1:8000/ordenes/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(orderData),
        });

        if (response.ok) {
            console.log('Orden creada exitosamente');
            loadOrders(); // Recargar la lista de órdenes después de crear una nueva
        } else {
            console.error('Error al crear la orden');
        }
    } catch (error) {
        console.error('Error:', error);
    }
});

async function loadOrders() {
    // Realiza la petición GET para obtener todas las órdenes
    const response = await fetch('http://127.0.0.1:8000/ordenes/', { method: 'GET' });
    const orders = await response.json();

    const ordersList = document.getElementById('orders');
    ordersList.innerHTML = ''; // Limpiar la lista actual

    // Itera sobre cada orden y la añade a la lista en el DOM
    orders.forEach(order => {
        const listItem = document.createElement('li');
        listItem.textContent = `Orden ID: ${order.ordenid}, Cliente ID: ${order.clienteId}, Fecha: ${order.fechaorden}, Cantidad de Prendas: ${order.totalprendas}, Estado: ${order.estado}, Pago: ${order.pago}`;
        // Añade más detalles de la orden si lo deseas

        ordersList.appendChild(listItem);
    });
}

// Llamar a loadOrders al cargar la página para mostrar la lista de órdenes existentes
document.addEventListener('DOMContentLoaded', () => {
    loadOrders();
});
