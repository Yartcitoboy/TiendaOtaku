document.addEventListener('DOMContentLoaded', function() {
    const addToCartButtons = document.querySelectorAll('.card .add-to-cart');
    const contenedorCarrito = document.getElementById('contenedor-carrito');
    const numerito = document.getElementById('numerito');
    const vaciarCarritoButton = document.getElementById('carrito-acciones-vaciar');
    const subtotalElement = document.getElementById('subtotal');

    // Objeto para almacenar los productos en el carrito
    let cartItems = {};

    // Función para manejar clic en añadir al carrito desde las tarjetas de producto
    function addToCartClicked(event) {
        event.preventDefault(); // Evitar el comportamiento predeterminado del enlace

        const card = event.target.closest('.card');
        if (!card) {
            console.error('No se encontró la tarjeta del producto.');
            return;
        }

        const nombreElement = card.querySelector('.card-body .card-title');
        const precioElement = card.querySelector('.card__preci--now');
        const imagenElement = card.querySelector('.card-img-top');
        const cantidadElement = card.querySelector('.cantidad');

        const nombre = nombreElement.innerText;
        const precio = parseFloat(precioElement.innerText.replace('$', '').replace(',', ''));
        const imagen = imagenElement.src;
        const cantidad = parseInt(cantidadElement.value);

        if (cartItems[nombre]) {
            cartItems[nombre].cantidad += cantidad;
        } else {
            cartItems[nombre] = { nombre, precio, imagen, cantidad };
        }

        updateCartUI();
        updateCartCounter();
        updateSubtotal();
        showConfirmation(nombre, cantidad);

        return false;
    }

    // Función para actualizar la interfaz del carrito
    function updateCartUI() {
        contenedorCarrito.innerHTML = ''; // Limpiar contenido del carrito

        // Recorrer los productos en el carrito y agregarlos al modal
        Object.values(cartItems).forEach(item => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${item.nombre}</td>
                <td>${item.precio}</td>
                <td>${item.cantidad}</td>
                <td><img src="${item.imagen}" style="max-width: 50px;" alt="Producto"></td>
            `;
            contenedorCarrito.appendChild(row);
        });
    }

    // Función para actualizar el contador de ítems en el carrito
    function updateCartCounter() {
        let totalItems = Object.values(cartItems).reduce((acc, item) => acc + item.cantidad, 0);
        numerito.innerText = totalItems;
    }

    // Función para actualizar el subtotal del carrito
    function updateSubtotal() {
        let subtotal = Object.values(cartItems).reduce((acc, item) => acc + item.precio * item.cantidad, 0);
        subtotalElement.innerText = `Sub-Total: $${subtotal.toFixed(2)}`;
    }

    // Función para mostrar la confirmación de producto añadido al carrito
    function showConfirmation(nombre, cantidad) {
        Swal.fire({
            title: 'Producto añadido al carrito',
            text: `${nombre} x ${cantidad}`,
            icon: 'success',
            showConfirmButton: false,
            timer: 1500
        });
    }

    // Añadir evento clic a cada botón de añadir al carrito
    addToCartButtons.forEach(button => {
        button.addEventListener('click', addToCartClicked);
    });

    // Vaciar carrito
    vaciarCarritoButton.addEventListener('click', () => {
        cartItems = {}; // Vaciar el objeto del carrito
        updateCartUI();
        updateCartCounter();
        updateSubtotal();
    });

});
