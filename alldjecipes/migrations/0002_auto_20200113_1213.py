# Generated by Django 3.0.2 on 2020-01-13 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alldjecipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='downvote',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='total',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='upvote',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='total',
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvoter', models.IntegerField(default=0)),
                ('downvoter', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alldjecipes.Comment')),
                ('recipe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alldjecipes.Recipe')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
