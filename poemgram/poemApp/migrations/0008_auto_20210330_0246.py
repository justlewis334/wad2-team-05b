# Generated by Django 2.2.17 on 2021-03-30 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poemApp', '0007_auto_20210330_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]