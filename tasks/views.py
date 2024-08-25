from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, UserRole 

# Create your views here.
def success_page(request):#Renderiza succes page
    return render(request, 'success.html')


def create_user(request):
    roles = UserRole.objects.all()
    if request.method == 'POST':
        # Capturar los datos del formulario
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role_id = request.POST.get('role')
        is_active = request.POST.get('is_active') == 'on'  

        # Validar los datos antes de crear el usuario
        if not username or not email or not password:
            messages.error(request, "Please fill out all required fields.")
        else:
            try:
                # Tomando rol de la base de datos (organizador, asistente y espectador)
                role = UserRole.objects.get(id=role_id) if role_id else None

                # Crear un nuevo usuario
                user = User(
                    username=username,
                    email=email,
                    password=password,  # HAY QUE HASHEAR, no se comoxd
                    role=role,
                    is_active=is_active
                )
                
                # Guardar el usuario en la base de datos
                user.save()

                messages.success(request, "User created successfully!")

                # Redirigir a una página de éxito o a la misma página
                return redirect('success_page')
            except UserRole.DoesNotExist:
                messages.error(request, "Selected role does not exist.")
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")

    # Renderizar la página con el formulario y los roles
    return render(request, 'user.html', {'roles': roles})

def view_home(request):#Renderiza la pagina de home
    return render(request, 'home.html' )