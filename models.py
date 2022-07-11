from django.db import models

class Lugat(models.Model):

    inglizcha = models.CharField('Inglizcha', max_length=150)
    uzbekcha = models.CharField("O'zbekcha", max_length=160)
