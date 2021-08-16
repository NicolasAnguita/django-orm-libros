from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('libros/<int:my_val>', views.libros),
    path('autores', views.autor),
]
