from .views import index, baixarVideos
from django.urls import path

urlpatterns = [
    path('', index, name='home'),
    path('baixar/', baixarVideos, name='baixarVideos'),
]
