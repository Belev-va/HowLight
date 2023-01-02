from django.db import models
from datetime import date

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    img = models.ImageField(upload_to='product', null=True, blank=True, verbose_name='Изображение')
    body = models.TextField()
    date = models.DateField()
    likes = models.IntegerField(default=0)
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.title