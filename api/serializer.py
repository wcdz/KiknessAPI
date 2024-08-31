from rest_framework import serializers
from models import ViewEstudiantes

class ViewEstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewEstudiantes
        fields = '__all__'
   
