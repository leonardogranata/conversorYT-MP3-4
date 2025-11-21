from .views import index
from django.urls import path

urlpatterns = [
    path('home/', index, name='home'),
]
