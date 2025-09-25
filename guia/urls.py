from django.urls import path
from .views import home, preview_procedure, procedures_list

urlpatterns = [
    path('', home, name='home'),
    path('preview/', preview_procedure, name='preview_procedure'),
    path('procedimentos/', procedures_list, name='procedures_list'),
]
