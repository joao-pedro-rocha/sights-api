# Generated by Django 4.1.7 on 2023-02-20 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('opening_hours', models.TextField(verbose_name='Opening hours')),
                ('minimum_age', models.IntegerField(verbose_name='Minimum age')),
            ],
        ),
    ]
