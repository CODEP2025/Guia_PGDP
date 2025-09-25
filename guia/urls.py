from django.urls import path
from .views import home, preview_procedure

urlpatterns = [
    path('', home, name='home'),
    path('preview/', preview_procedure, name='preview_procedure'),
]
