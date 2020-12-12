from django.db import models

# Create your models here.
class Product(models.Model):
    tittle = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.tittle