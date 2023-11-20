from django.db import models
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
from datetime import date
# from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='Author'
    )

    descr = models.TextField(verbose_name='Описание')
    content = RichTextField(null=True, blank=True, verbose_name='Контент')
    # content = RichTextUploadingField(null=True, blank=True)
    date = models.DateField(verbose_name='Дата')
    img = models.ImageField(upload_to='news', null=True, blank=True, verbose_name='Изображение')

    @property
    def img_preview(self):
        if self.img:
            _thumbnail = get_thumbnail(self.img,
                                   '300x150',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""

    def __str__(self):
        return self.title