from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik')
    publishing_date = models.DateTimeField(verbose_name='Yayınlanma Tarihi')

    def __str__(self):
        return self.title + " - " + self.content

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'kimlik':self.id})
        # return '/post/detail/' + str(self.id)
        # return '/post/detail/{}'.format(self.id)
