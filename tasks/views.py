from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import User, UserRole, Event
from django.utils import timezone


# Create your views here.
def create_event(request):#Renderiza pagina de creacion de eventos
    if request.method == 'POST':
        # Obtén los datos del formulario del request
        name = request.POST.get('name')
        description = request.POST.get('description')
        location = request.POST.get('location')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        organizer_id = request.POST.get('organizer')
        max_participants = request.POST.get('max_participants')
        is_public = 'is_public' in request.POST  # Obtén el valor del checkbox (True si está marcado)

        # Realiza validaciones adicionales si es necesario
        if not name or not start_date or not end_date:
            # Devuelve un error si faltan campos requeridos
            return render(request, 'event.html', {'users': User.objects.all(), 'error': 'Please fill out all required fields.'})

        # Trata de obtener el organizador si se proporciona uno
        organizer = None
        if organizer_id:
            organizer = User.objects.filter(id=organizer_id).first()

        # Crea una nueva instancia del modelo Event
        event = Event(
            name=name,
            description=description,
            location=location,
            start_date=start_date,
            end_date=end_date,
            organizer=organizer,
            max_participants=max_participants if max_participants else None,
            is_public=is_public,
        )

        # Guarda el nuevo evento en la base de datos
        event.save()

        # Redirige a una página de éxito o a la lista de eventos después de la creación exitosa
        return redirect('success_page')  # Asegúrate de tener una URL llamada 'success_page'

    # Si la solicitud es GET, simplemente muestra el formulario de creación de eventos
    users = User.objects.all()  # Obtiene todos los usuarios para mostrar en el campo de organizador
    return render(request, 'event.html', {'users': users})

def success_page(request):#Renderiza pagina succes
    return render(request, 'success.html')


def create_user(request):
    roles = UserRole.objects.all() #Obtener roles de la base
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
                # Tomando rol del formulario(organizador, asistente y espectador)
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
    events = Event.objects.all()  # Obteniendo eventos de la base
    return render(request, 'home.html', {'events': events})


def delete_event(request, event_id): #Func pa eliminar eventos basandose en id
    if request.method == 'POST':
        event = get_object_or_404(Event, id=event_id)
        event.delete()
        return redirect('home')  # Redirige a la página de inicio o a otra página deseada
    return redirect('home')