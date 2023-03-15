from django.db import models


class Adress(models.Model):
    
    line_1 = models.CharField(verbose_name='Line 1', max_length=150)
    line_2 = models.CharField(verbose_name='Line 2', max_length=150)
    city = models.CharField(verbose_name='City', max_length=150)
    state = models.CharField(verbose_name='State', max_length=80)
    country = models.CharField(verbose_name='Country', max_length=80)
    latitude = models.IntegerField(verbose_name='Latitude', null=True,
                                   blank=True)
    longitude = models.IntegerField(verbose_name='Longitude', null=True,
                                    blank=True)

    def __str__(self):
        return self.line_1
