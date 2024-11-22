from django.shortcuts import render,redirect
#ESTO DE ABAJO NO LO PESQUE YA QUE ES PARTE DEL LOGUELO
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import Usuario
# Create your views Login/Register here.

# CREAR VISTA (ESTO HACE QUE LA PÁGINA SE VE DENTRO DEL ENTORNO DE DJANGO, SI NO LO HACES TE DARA ERROR Y NO SE VERA)
def index(request):
    return render(request, 'web/index.html')

@login_required # ESTO IGNORALO YA QUE ES PARTE DEL LOGUEO
def ofertas(request):
    return render(request, 'web/vistas/Ofertas.html')

@login_required
def productos(request):
    return render(request, 'web/vistas/Productos.html')

@login_required
def perfil(request):
    return render(request, 'web/vistas/perfil.html')



def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            username = user_creation_form.cleaned_data['username']
            password = user_creation_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('perfil')
    return render(request, 'registration/register.html', data)

def login(request, user):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next', 'perfil')
                return redirect(next_url)
    else:
        form = AuthenticationForm()
        next_url = request.GET.get('next', 'perfil')
    return render(request, 'registration/login.html', {'form': form})

#LO DE ABAJO ES PARA ORACLE , NO LO TOQUES POR QUE TODAVIA DEBO ARREGLARLO

# def register_old(request):
#     if request.method == 'POST':
#         username = request.POST.get("username")
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         email = request.POST.get("email")
#         password = request.POST.get("password")  # Asegúrate de capturar el campo password correctamente

#         print(username, first_name, last_name, email, password)

#         if Usuario.objects.filter(username=username).exists():
#             # Manejar el caso donde el usuario ya existe
#             return render(request, 'registration/register.html')

#         # Crear un nuevo usuario en la base de datos
#         usuario = Usuario.objects.create(
#             username=username,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             password=password
#         )

#         return redirect('perfil')  
#     else:
#         return render(request, 'web/vistas/perfil.html')

def perfil(request):
    if request.user.is_authenticated:
        return render(request, 'web/vistas/perfil.html', {'user': request.user})
    else:
        return redirect('login')

def exit(request):
    logout(request)
    return redirect('index')




