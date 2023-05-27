# Generated by Django 4.1.5 on 2023-03-13 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Festivos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('festivo', models.DateField(max_length=10, verbose_name='Festivo')),
            ],
            options={
                'ordering': ['festivo'],
            },
        ),
    ]
