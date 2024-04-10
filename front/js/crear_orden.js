document.getElementById('add-order-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    // Obtén los valores de los campos del formulario
    const clienteid = document.getElementById('clienteId').value;
    const totalprendas = document.getElementById('totalprendas').value;
    const estado = document.getElementById('estado').value;
    const pago = document.getElementById('pago').value;
    const now = new Date();
    const fecha = now.toISOString().slice(0, 19).replace('T', ' ');
    // Asumiendo que tienes otros campos como fechaOrden, etc., añádelos aquí

    // Construye el objeto con los datos recogidos
    const orderData = {
        clienteid: clienteid,
        fechaorden: fecha,
        totalprendas: totalprendas,
        estado: estado,
        pago: pago
        // Añade otros campos aquí según tu modelo de datos
    };

    try {
        // Realiza la petición POST para crear la nueva orden
        const response = await fetch('http://127.0.0.1:8000/orden/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(orderData),
        });

        if (response.ok) {
            console.log('Orden creada exitosamente');
        } else {
            console.error('Error al crear la orden');
        }
    } catch (error) {
        console.error('Error:', error);
    }
    location.reload()
});