$(document).ready(function(){
    // Inicializar el slider principal que muestra la imagen grande
    $('.slider-for').slick({
        slidesToShow: 1, // Mostrar solo una imagen grande a la vez
        slidesToScroll: 1, // Desplazar una imagen a la vez
        arrows: false, // No mostrar flechas de navegación
        fade: true, // Aplicar un efecto de desvanecimiento al cambiar de imagen
        asNavFor: '.slider-nav' // Vincular este slider con el de navegación
    });

    // Inicializar el slider de navegación que muestra las miniaturas
    $('.slider-nav').slick({
        slidesToShow: 5, // Mostrar cinco miniaturas a la vez
        slidesToScroll: 1, // Desplazar una miniatura a la vez al hacer clic en las flechas
        asNavFor: '.slider-for', // Vincular este slider con el slider principal
        dots: true, // Mostrar puntos de navegación
        centerMode: true, // Centrar la miniatura seleccionada
        focusOnSelect: true // Permitir la selección de miniaturas con clic
    });

    // Evento para navegar a una imagen específica al hacer clic en un enlace
    $('a[data-slide]').click(function(e) {
        e.preventDefault(); // Prevenir el comportamiento predeterminado del enlace
        var slideno = $(this).data('slide'); // Obtener el número de la imagen desde el atributo data-slide
        $('.slider-nav').slick('slickGoTo', slideno - 1); // Navegar a la imagen correspondiente
    });
});
