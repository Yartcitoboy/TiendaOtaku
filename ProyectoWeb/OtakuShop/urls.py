from django.urls import path
from .views import index, perfil, ofertas, productos, exit, register, login
#ESTO VA DE LA MANO CON LAS VIEW.PY DE ABAJO , ESTO SIRVE CUANDO BUSCA EB EL BUSCADOR DE GOOGLE. EJ(HOME/PRODUCTOS) Y ESTO TE LLEVA A PRODUCTOS
urlpatterns = [
    path('',index,name='index'),
    path('productos/',productos,name='productos'),
    path('ofertas/',ofertas,name='ofertas'),
    path('perfil/',perfil,name='perfil'),
    path('login/',login, name='login'),
    path('logout/' ,exit, name='exit'),
    path('register/' ,register, name='register'),
    # path('register_old/' ,register_old, name='register_old'),
]