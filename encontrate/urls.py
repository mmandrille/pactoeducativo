from django.conf.urls import url
from django.urls import path
#Import personales
from . import views

app_name = 'encontrate'
urlpatterns = [
    path('', views.encontrate, name='encontrate'),
    path('<int:album_id>/', views.album, name='album'),
]