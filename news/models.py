from django.db import models
from datetime import date

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    img = models.ImageField(upload_to='news', null=True, blank=True, verbose_name='Изображение')
    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title