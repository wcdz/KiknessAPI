from django.db import models

# TODO: Definir la lista de las vistas que requiere la aplicación
'''
view_estudiantes
view_alertas
'''        
class ViewEstudiantes (models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    cod_estudiante = models.CharField(max_length=9, null=True)
    nombres_estudiante = models.CharField(max_length=100, null=True)
    apellidos_estudiante = models.CharField(max_length=100, null=True)
    anio_ingreso = models.CharField(max_length=100, null=True)
    estado_estudiante = models.IntegerField(default=1)
    perfil_estudiante = models.CharField(max_length=100, null=True)
    captura_biometrica = models.CharField(max_length=255, null=True)
    nombre_nivel_academico = models.CharField(max_length=100, null=True)
    nombre_facultad = models.CharField(max_length=100, null=True)
    nombre_especialidad = models.CharField(max_length=100, null=True)
    class Meta:
        managed = False  # Indica a Django que este modelo no es gestionado directamente por Django
        db_table = 'view_estudiantes'  # Nombre de la vista en la base de datos
        