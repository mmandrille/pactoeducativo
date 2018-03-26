from django.conf.urls import url
from django.urls import path
#Import personales
from . import views

app_name = 'core'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url('^faq/$', views.faq, name='faq'),
    url('^biblioteca/$', views.biblioteca, name='biblioteca'),
    path('biblioteca/<int:archivo_id>', views.archivo, name='archivo'),

    url('^noticias/$', views.noticias, name='noticias'),
    
    url('^encontrate/$', views.encontrate, name='encontrate'),
]