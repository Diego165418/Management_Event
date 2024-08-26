from django.urls import path
from .views import view_home, create_user, success_page, create_event, delete_event, login

urlpatterns = [
    path('home/', view_home, name='home'),
    path('success/', success_page, name='success_page'),
    path('new_user/', create_user, name='create_user_page'),
    path('new_event/', create_event, name="create_event_page"),
    path('delete_event/<int:event_id>/', delete_event, name="delete_event"),
    path('login/', login, name="login_page")
    
] 