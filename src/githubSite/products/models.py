from django.db import models

# Create your models here.
class Product(models.Model):
    """modelo de producto

    Args:
        models ([type]): [description]

    Returns:
        [str]: [returns title ]
    """
    title = models.CharField(max_length = 120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default = True)
    def __str__(self):
        return self.title