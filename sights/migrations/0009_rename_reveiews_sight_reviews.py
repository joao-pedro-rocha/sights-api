# Generated by Django 4.1.7 on 2023-03-20 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sights', '0008_alter_sight_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sight',
            old_name='reveiews',
            new_name='reviews',
        ),
    ]
