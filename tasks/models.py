from django.db import models

# Create your models here.
class Tarea(models.Model):
    tid= models.IntegerField()
    tname=models.CharField(max_length=100)
    tdesc=models.CharField(max_length=500)
    euser=models.CharField(max_length=100)
    class Meta:
        db_table="tareas"
