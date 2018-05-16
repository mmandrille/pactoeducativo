from django.conf.urls import url
from django.urls import path
#Import personales
from . import views

app_name = 'biblioteca'
urlpatterns = [
    path('', views.biblioteca, name='biblioteca'),
    path('<int:archivo_id>/', views.archivo, name='archivo'),
]