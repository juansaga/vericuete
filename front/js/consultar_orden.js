async function loadOrders() {
    // Realiza la petición GET para obtener todas las órdenes
    const response = await fetch('http://127.0.0.1:8000/orden/', { method: 'GET' });
    const orders = await response.json();

    const ordersList = document.getElementById('orders');
    ordersList.innerHTML = ''; // Limpiar la lista actual

    // Itera sobre cada orden y la añade a la lista en el DOM
    orders.forEach(order => {
        const listItem = document.createElement('li');
        listItem.textContent = `Orden ID: ${order.ordenid}, Cliente ID: ${order.clienteid}, Fecha: ${order.fechaorden}, Cantidad de Prendas: ${order.totalprendas}, Estado: ${order.estado}, Pago: ${order.pago}`;
        // Añade más detalles de la orden si lo deseas

        ordersList.appendChild(listItem);
    });
}

// Llamar a loadOrders al cargar la página para mostrar la lista de órdenes existentes
document.addEventListener('DOMContentLoaded', () => {
    loadOrders();
});