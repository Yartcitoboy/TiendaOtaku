// Función para filtrar tarjetas por categoría
function filterCards(category) {
    // Obtener todas las tarjetas con la clase 'card'
    const cards = document.getElementsByClassName('card');
    // Iterar a través de todas las tarjetas
    for (let card of cards) {
        // Si la categoría es una cadena vacía o la tarjeta tiene una clase que coincide con la categoría especificada
        if (category === '' || card.classList.contains('card-' + category)) {
            // Mostrar la tarjeta
            card.style.display = 'inline-block';
        } else {
            // Ocultar la tarjeta
            card.style.display = 'none';
        }
    }
}

// Función para filtrar tarjetas por precio
function filterCardsByPrice(price) {
    // Obtener todas las tarjetas con la clase 'card'
    const cards = document.getElementsByClassName('card');
    // Iterar a través de todas las tarjetas
    for (let card of cards) {
        // Obtener el precio de la tarjeta desde el atributo 'data-precio' y convertirlo a un número entero
        const cardPrice = parseInt(card.getAttribute('data-precio'));
        // Si el precio especificado es NaN (no es un número) o el precio de la tarjeta es menor o igual al precio especificado
        if (isNaN(price) || cardPrice <= price) {
            // Mostrar la tarjeta
            card.style.display = 'inline-block';
        } else {
            // Ocultar la tarjeta
            card.style.display = 'none';
        }
    }
}

// Función para reiniciar los filtros
function resetFilters() {
    // Obtener todas las tarjetas con la clase 'card'
    const cards = document.getElementsByClassName('card');
    // Iterar a través de todas las tarjetas
    for (let card of cards) {
        // Mostrar todas las tarjetas
        card.style.display = 'inline-block';
    }
    // Reiniciar el campo de precio a una cadena vacía
    document.getElementById('precio').value = '';
}
