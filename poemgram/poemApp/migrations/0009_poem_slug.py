# Generated by Django 2.2.17 on 2021-03-30 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poemApp', '0008_auto_20210330_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
