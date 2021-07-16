from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UploadFileSerializer
from .models import UploadFile
from deals_api_project.settings import MEDIA_ROOT
from .csv_handler import csv_handler
import csv
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'upload_files': reverse('api:uploadfiles', request=request, format=format)
    })


class UploadFileView(generics.ListCreateAPIView):
    serializer_class = UploadFileSerializer
    queryset = UploadFile.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', )

    def perform_create(self, serializer):
        serializer.validated_data['file'], serializer.validated_data['date_from'], serializer.validated_data['date_to']\
            = csv_handler(serializer.validated_data['file'], UploadFile.objects.all().count())
        if serializer.is_valid():
            return serializer.save()


class CustomersFromFileView(generics.ListAPIView):
    """Вывод списка клиентов из обработанного файла"""
    queryset = UploadFile.objects.all()
    serializer_class = UploadFileSerializer

    def get(self, request, pk):
        file = UploadFile.objects.get(id=pk).file
        with open(MEDIA_ROOT+'/'+str(file), encoding='utf-8') as f:
            reader = csv.reader(f)
            customers = []
            row1 = next(reader)
            customer = {}
            for row in reader:
                customer['username'] = row[0]
                customer['spent_money'] = row[1]
                customer['gems'] = [row[2].split()]
                customers.append(customer.copy())

        return Response(customers)

