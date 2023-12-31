from django.urls import path
from .views import manipular_dados, export_to_elasticsearch, retrieve_data_from_elasticsearch, remover_dado, remover_dado_elastic

urlpatterns = [
    path('', manipular_dados, name='manipular_dados'),
    path('export_to_elasticsearch/', export_to_elasticsearch,
         name='export_to_elasticsearch'),
    path('retrieve_data_from_elasticsearch/', retrieve_data_from_elasticsearch,
         name='retrieve_data_from_elasticsearch'),
    path('remover_dado/<int:dado_id>/', remover_dado, name='remover_dado'),
    path('remover_dado_elastic/<str:document_id>/',
         remover_dado_elastic, name='remover_dado_elastic'),


]
