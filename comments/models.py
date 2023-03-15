from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name='User',
                             on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Comment')
    date_and_hour = models.DateTimeField(verbose_name='Date and hour',
                                         auto_now_add=True)
    approved = models.BooleanField(verbose_name="It's approved?", default=True)

    def __str__(self):
        return self.user.username
