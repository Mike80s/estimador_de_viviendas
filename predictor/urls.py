from django.urls import path
from . import views

urlpatterns = [
    path('', views.predecir_precio, name='predecir_precio'),]

