from django.db import models


class Revo(models.Model):
    ball = models.CharField('ballast', max_length=50)
    write = models.TextField('about me')

    def __str__(self):
        return self.ball