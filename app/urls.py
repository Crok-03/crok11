from django.urls import path
from .views import upload_json_view, records_list_view

urlpatterns = [
    path('', upload_json_view, name='upload_json'),
    path('records/', records_list_view, name='records_list'),
]