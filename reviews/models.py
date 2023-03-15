from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):

    user = models.ForeignKey(User, verbose_name='User',
                             on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Comment', null=True, blank=True)
    grade = models.DecimalField(verbose_name='Grade', max_digits=3,
                                decimal_places=2)
    date_and_hour = models.DateTimeField(verbose_name='Date and hour',
                                         auto_now_add=True)
    
    def __str__(self):
        return self.user.username
