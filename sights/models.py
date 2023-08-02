from django.db import models
from attractions.models import Attraction
from comments.models import Comment
from reviews.models import Review
from adresses.models import Adress


class DocumentOfIntent(models.Model):
    description = models.CharField(verbose_name='Description', max_length=3000)

    def __str__(self):
        return f'{self.description[:50]}...'


class Sight(models.Model):
    name = models.CharField(verbose_name='Name', max_length=150)
    description = models.TextField(verbose_name='Description')
    approved = models.BooleanField(verbose_name="It's approved?",
                                   default=False)
    attractions = models.ManyToManyField(Attraction, 
                                         verbose_name='Attractions')
    comments = models.ManyToManyField(Comment, verbose_name='Comments')
    reviews = models.ManyToManyField(Review, verbose_name='Review')
    adress = models.ForeignKey(Adress, verbose_name='Adress',
                               on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(verbose_name='Image', upload_to='sights',
                              null=True, blank=True)
    document_of_intent = models.OneToOneField(
        DocumentOfIntent,
        verbose_name='Document of intent',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.name
    
    # Para ser chamado no serializer
    @property
    def complete_description_2(self):
        return f'{self.name} - {self.description}'
