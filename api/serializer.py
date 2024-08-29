from rest_framework import serializers
from models import ViewEstudiantes

class ViewEstudiantesSerializer(serializers.ModelSerializer):
    model = ViewEstudiantes
    fields = '__all__'
    
