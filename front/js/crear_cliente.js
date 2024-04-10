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
             // Recargar la lista de clientes después de agregar
        } else {
            console.error('Error al agregar cliente');
        }
    } catch (error) {
        console.error('Error:', error);
    }
    location.reload()
});
