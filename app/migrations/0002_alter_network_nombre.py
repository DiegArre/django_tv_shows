# Generated by Django 3.2.5 on 2021-08-19 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='network',
            name='nombre',
            field=models.CharField(max_length=45, unique=True),
        ),
    ]
