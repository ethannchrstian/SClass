from django.urls import path
from .views import view

urlpatterns = [
    path('', view, name='app_blog') #ini lu bisa ganti nama
]