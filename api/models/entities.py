from django.db import models


class Facultades(models.Model):
    id_facultad = models.AutoField(primary_key=True)
    nombre_facultad = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.id_facultad


class NivelesAcademicos(models.Model):
    id_nivel_academico = models.AutoField(primary_key=True)
    nombre_nivel_academico = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.id_nivel_academico


class Especialidades(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    nombre_especialidad = models.CharField(max_length=100, null=True)
    id_facultad = models.ForeignKey(
        Facultades, on_delete=models.SET_NULL, db_column="id_facultad", null=True
    )
    id_nivel_academico = models.ForeignKey(
        NivelesAcademicos,
        on_delete=models.SET_NULL,
        db_column="id_nivel_academico",
        null=True,
    )

    def __str__(self):
        return self.id_especialidad


class Estudiantes(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    cod_estudiante = models.CharField(max_length=9, null=True)
    nombres_estudiante = models.CharField(max_length=100, null=True)
    apellidos_estudiante = models.CharField(max_length=100, null=True)
    anio_ingreso = models.CharField(max_length=100, null=True)
    estado_estudiante = models.IntegerField(default=1)
    perfil_estudiante = models.CharField(max_length=100, null=True)
    captura_biometrica = models.CharField(max_length=255, null=True)
    id_facultad = models.ForeignKey(
        Facultades, on_delete=models.SET_NULL, db_column="id_facultad", null=True
    )
    id_nivel_academico = models.ForeignKey(
        NivelesAcademicos,
        on_delete=models.SET_NULL,
        db_column="id_nivel_academico",
        null=True,
    )
    id_especialidad = models.ForeignKey(
        Especialidades,
        on_delete=models.SET_NULL,
        db_column="id_especialidad",
        null=True,
    )

    def __str__(self):
        return self


class AuditoriaIngresos(models.Model):
    id_ingreso = models.AutoField(primary_key=True)
    fecha_ingreso = models.DateField(auto_now_add=True)
    hora_ingreso = models.TimeField(auto_now_add=True)
    id_estudiante = models.ForeignKey(
        Estudiantes, on_delete=models.SET_NULL, db_column="id_estudiante", null=True
    )

    def __str__(self):
        return self.id_ingreso


class Alertas(models.Model):
    id_alerta = models.AutoField(primary_key=True)
    fecha_alerta = models.DateField(auto_now_add=True)
    hora_alerta = models.TimeField(auto_now_add=True)
    detalle_alerta = models.CharField(max_length=255, null=True)
    estado_alerta = models.IntegerField(default=1)
    foto_captura = models.CharField(max_length=255, null=True)
    id_estudiante = models.ForeignKey(
        Estudiantes, on_delete=models.SET_NULL, db_column="id_estudiante", null=True
    )

    def __str__(self):
        return self.id_alerta


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    correo = models.CharField(max_length=100, null=True)
    nombre = models.CharField(max_length=50, null=True)
    apellido = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.id_usuario


class EnvioAlertas(models.Model):
    id_envio_alertas = models.AutoField(primary_key=True)
    id_alerta = models.ForeignKey(
        Alertas, on_delete=models.SET_NULL, db_column="id_alerta", null=True
    )
    id_usuario = models.ForeignKey(
        Usuarios, on_delete=models.SET_NULL, db_column="id_usuario", null=True
    )

    def __str__(self):
        return self.id_envio_alertas
