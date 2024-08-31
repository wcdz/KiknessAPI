from rest_framework import serializers
from .models import ViewEstudiantes, Estudiantes, Facultades, NivelesAcademicos

class ViewEstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewEstudiantes
        fields = '__all__'
   
class EstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiantes
        fields = '__all__'
   
class FacultadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultades
        fields = '__all__'
        
class NivelesAcademicosSerializaer(serializers.ModelSerializer):
    class Meta:
        model = NivelesAcademicos
        fields = '__all__'