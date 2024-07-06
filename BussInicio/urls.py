from django.urls import path 
from BussInicio import views

# Otros aconsejan usar  --> From * import views


urlpatterns = [
    path('', views.Home, name='home')
]
