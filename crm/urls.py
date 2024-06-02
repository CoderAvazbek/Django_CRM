from django.urls import path
from .views import home, logout_user, register_user

urlpatterns = [

    path('', home, name='home'),
    path('regsiter/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),

]