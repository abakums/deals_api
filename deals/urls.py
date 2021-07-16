from django.urls import path
from .views import UploadFileView, CustomersFromFileView, api_root

app_name = 'deals'

urlpatterns = [
    path('upload_file/', UploadFileView.as_view(), name='uploadfiles'),
    path('upload_file/<int:pk>/', CustomersFromFileView.as_view(), name='customers'),
    path('', api_root)
]