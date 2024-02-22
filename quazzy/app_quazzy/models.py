from django.db import models

class Publication(models.Model):
    text = models.TextField()
    arq = models.FileField(upload_to="imagens")
