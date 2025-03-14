from django.urls import path
from .views import view

urlpatterns = [
    path('', view, name='app_landing') #ini lu bisa ganti nama
]