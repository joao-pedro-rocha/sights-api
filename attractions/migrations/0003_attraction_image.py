# Generated by Django 4.1.7 on 2023-02-24 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0002_alter_attraction_minimum_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='attraction', verbose_name='Image'),
        ),
    ]
