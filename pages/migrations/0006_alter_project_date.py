# Generated by Django 4.1.4 on 2022-12-26 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_project_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(),
        ),
    ]
