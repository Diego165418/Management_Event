from django.urls import path
from .views import view_home, create_user, success_page, create_event

urlpatterns = [
    path('home/', view_home, name='home'),
    path('success/', success_page, name='success_page'),
    path('new_user/', create_user, name='create_user_page'),
    path('new_event/', create_event, name="create_event_page"),
] 