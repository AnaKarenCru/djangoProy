from django.db import models

class Alumnos(models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)
    matricula = models.IntegerField(null=False)
    campus = models.TextField(max_length=20)
    carrera = models.TextField(max_length=100)
    semestre = models.IntegerField(null=False)
    materias = models.IntegerField(null=False)

