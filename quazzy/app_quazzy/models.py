from django.db import models

class Publication(models.Model):
    nome = models.TextField()
    text = models.TextField()
    #arq = models.FileField(upload_to="imagens")
