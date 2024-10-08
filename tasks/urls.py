from django.urls import path
from .views import view_home, create_user, success_page, create_event, delete_event, user_login, view_test

urlpatterns = [
    path('home/', view_home, name='home'),
    path('success/', success_page, name='success_page'),
    path('new_user/', create_user, name='create_user_page'),
    path('new_event/', create_event, name="create_event_page"),
    path('delete_event/<int:event_id>/', delete_event, name="delete_event"),
    path('login/', user_login, name="login_page"),
    path ('protected/', view_test, name="protected_view" )
    
]