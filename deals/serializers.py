from rest_framework import serializers
from .models import UploadFile


class UploadFileSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:customers')

    class Meta:

        model = UploadFile
        fields = ['id', 'upload_name', 'url', 'comment', 'file']
