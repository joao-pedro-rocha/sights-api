from django.db import models


class Attraction(models.Model):
   
    name = models.CharField(verbose_name='Name', max_length=150)
    description = models.TextField(verbose_name='Description')
    opening_hours = models.TextField(verbose_name='Opening hours')
    minimum_age = models.IntegerField(verbose_name='Minimum age', default=10)
    image = models.ImageField(verbose_name='Image', upload_to='attraction',
                                null=True, blank=True)

    def __str__(self):
        return self.name
