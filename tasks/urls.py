from django.urls import path
from .views import view_home, create_user

urlpatterns = [
    path('home/', view_home, name='home'),
    path('create_user/', create_user, name='c_user')
] 