from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=128)  # Opcionalmente puedes usar models.PasswordField si lo prefieres, pero debes importar otra cosa para que funcione

    def __str__(self):
        return self.username
    
# ACA TU CREAS LA TABLAS PARA USARLA EN LA BASE DE DATOS, EN ESTE CASO SOLO USE UN USUARIO COMO TABLA, YA QUE NO TUVE TIEMPO Y NO QUERIA HACERLO XD
# PERO SI FUERA COMO ENLA PRUEBA Y LA PAGINA ACTUAL FALTARIA TABLA PRODUCTO Y OTRAS COSAS MÁS.