# Generated by Django 3.0.2 on 2020-01-16 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alldjecipes', '0003_auto_20200113_1217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='difficulty_level',
            new_name='difficulty',
        ),
    ]
