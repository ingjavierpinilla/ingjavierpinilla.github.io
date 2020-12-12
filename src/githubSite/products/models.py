from django.db import models

# Create your models here.
class Product(models.Model):
    """modelo de producto

    Args:
        models ([type]): [description]

    Returns:
        [str]: [returns title ]
    """
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title