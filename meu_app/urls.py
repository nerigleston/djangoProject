from django.urls import path
from .views import manipular_dados, export_csv, remover_dado

urlpatterns = [
    path('manipular_dados/', manipular_dados, name='manipular_dados'),
    path('export_csv/', export_csv, name='export_csv'),
    path('remover_dado/<int:dado_id>/', remover_dado, name='remover_dado'),
]
