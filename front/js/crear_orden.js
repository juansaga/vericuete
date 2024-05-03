document.getElementById('add-order-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const clienteid = document.getElementById('clienteId').value;
    const totalprendas = document.getElementById('totalprendas').value;
    const estado = document.getElementById('estado').value;
    const pago = document.getElementById('pago').value;
    const now = new Date();
    const fecha = now.toISOString().slice(0, 19).replace('T', ' ');
  


    const orderData = {
        clienteid: clienteid,
        fechaorden: fecha,
        totalprendas: totalprendas,
        estado: estado,
        pago: pago
    };

    try {
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