import json


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import IntegrityError

from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout, authenticate, login as auth_login
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

from tasks.models import User, UserRole, Event
from django.contrib.auth import authenticate, login

# Create your views here.
def view_test (request):
    if request.user.is_authenticated:
        return render(request,'protected.html')
    else:
        return redirect('home')

def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(request.POST)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
            # print(request.POST)
            


def user_logiin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirige a la página de inicio después del login exitoso
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
        'messages': json.dumps([msg.message for msg in messages.get_messages(request)]),  # Convertir los mensajes a JSON
    }
    return render(request, 'login.html', context)

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
        is_public = 'is_public' in request.POST 

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


# def create_user(request):
#     roles = UserRole.objects.all()  # Obtener roles de la base
#     messages = []
    
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         role_id = request.POST.get('role')
#         is_active = request.POST.get('is_active') == 'on'

#         if not username or not email or not password:
#             messages.append("Please fill out all required fields.")
#         else:
#             try:
#                 if User.objects.filter(email=email).exists():
#                     messages.append("Error: Ya existe un usuario con este correo electrónico.")
#                 elif User.objects.filter(username=username).exists():
#                     messages.append("Error: Ya existe un usuario con este nombre de usuario.")
#                 else:
#                     role = UserRole.objects.get(id=role_id) if role_id else None
#                     user = User(
#                         username=username,
#                         email=email,
#                         password=make_password(password),
#                         role=role,
#                         is_active=is_active
#                     )
#                     user.save()
#                     messages.append("User created successfully!")
#                     return redirect('success_page')
#             except UserRole.DoesNotExist:
#                 messages.append("Selected role does not exist.")
#             except IntegrityError as e:
#                 messages.append(f"An error occurred: {str(e)}")
#             except Exception as e:
#                 messages.append(f"An unexpected error occurred: {str(e)}")

#     return render(request, 'user.html', {
#         'roles': roles,
#         'messages': json.dumps(messages)  # Pasar mensajes como JSON
#     })
User = get_user_model()  # Obtener el modelo de usuario personalizado

def create_user(request):
    roles = UserRole.objects.all()  # Obtener roles de la base de datos
    messages_list = []  # Renombrado para evitar conflictos con 'messages' de Django
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role_id = request.POST.get('role')
        is_active = request.POST.get('is_active') == 'on'

        if not username or not email or not password:
            messages_list.append("Please fill out all required fields.")
        else:
            try:
                if User.objects.filter(email=email).exists():
                    messages_list.append("Error: Ya existe un usuario con este correo electrónico.")
                elif User.objects.filter(username=username).exists():
                    messages_list.append("Error: Ya existe un usuario con este nombre de usuario.")
                else:
                    role = UserRole.objects.get(id=role_id) if role_id else None
                    
                    # Usar el UserManager para crear un usuario
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password,
                        role=role
                    )
                    print(user.is_active)
                    messages_list.append("User created successfully!")
                    login(request, user)
                    return redirect('success_page')
            except UserRole.DoesNotExist:
                messages_list.append("Selected role does not exist.")
            except IntegrityError as e:
                messages_list.append(f"An error occurred: {str(e)}")
            except Exception as e:
                messages_list.append(f"An unexpected error occurred: {str(e)}")

    return render(request, 'user.html', {
        'roles': roles,
        'messages': json.dumps(messages_list)  # Pasar mensajes como JSON
    })

# def create_user(request):
#     if request.method == 'GET':
#         return render(request, 'user.html', {'form': CustomUserCreationForm})    
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user (username=request.POST['username'], email=request.POST['email'], password=request.POST['password1']) 
#             form = CustomUserCreationForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 login(request, user)
#                 return redirect('home')



def view_home(request):#Renderiza la pagina de home
    events = Event.objects.all()  # Obteniendo eventos de la base
    return render(request, 'home.html', {'events': events})

def delete_event(request, event_id): #Func pa eliminar eventos basandose en id
    if request.method == 'POST':
        event = get_object_or_404(Event, id=event_id)
        event.delete()
        return redirect('home')  # Redirige a la página de inicio o a otra página deseada
    return redirect('home')