# Generated by Django 4.1.4 on 2023-01-07 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='description',
            new_name='descr',
        ),
    ]
