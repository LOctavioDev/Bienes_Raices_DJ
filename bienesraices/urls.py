from django.contrib import admin
from django.urls import path
from task import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hola_web, name='hola_web'),
    path('quienEres/', views.quien_eres, name='quien_eres'),
    path('queUsas/', views.que_usas, name='que_usas'),
    path('misDatos/', views.mis_datos, name='mis_datos')
]