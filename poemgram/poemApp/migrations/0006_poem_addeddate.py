# Generated by Django 2.2.17 on 2021-03-30 00:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('poemApp', '0005_auto_20210330_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='addedDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]