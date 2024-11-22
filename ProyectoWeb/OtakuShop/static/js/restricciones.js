$(document).ready(function () {
  $("#nombre").on("input", function () {
    this.value = this.value.replace(/[^A-Za-z]/g, "");
  });

  $("#run").on("input", function () {
    this.value = this.value.replace(/\D/g, "");
  });

  $("#email").on("input", function () {
    this.value = this.value.replace(/[^A-Za-z]/g, "");
  });

  $("#fono").on("input", function () {
    this.value = this.value.replace(/\D/g, "");
  });

  $("#password").on("input", function () {
    this.value = this.value.replace(/[^A-Za-z]/g, "");
  });
});

//aca solo uso jquery para validar alguinas cosas del formulario, abajo de te dejo en js

// document.addEventListener("DOMContentLoaded", function () {
//   document.getElementById("nombre").addEventListener("input", function () {
//     this.value = this.value.replace(/[^A-Za-z]/g, "");
//   });

//   document.getElementById("run").addEventListener("input", function () {
//     this.value = this.value.replace(/\D/g, "");
//   });

//   document.getElementById("email").addEventListener("input", function () {
//     this.value = this.value.replace(/[^A-Za-z]/g, "");
//   });

//   document.getElementById("fono").addEventListener("input", function () {
//     this.value = this.value.replace(/\D/g, "");
//   });

//   document.getElementById("password").addEventListener("input", function () {
//     this.value = this.value.replace(/[^A-Za-z]/g, "");
//   });
// });

