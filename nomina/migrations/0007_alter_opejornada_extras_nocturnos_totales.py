# Generated by Django 4.2 on 2023-05-05 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0006_opejornada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opejornada',
            name='extras_nocturnos_totales',
            field=models.FloatField(default=0, verbose_name='Horas Extras Nocturnas'),
        ),
    ]
