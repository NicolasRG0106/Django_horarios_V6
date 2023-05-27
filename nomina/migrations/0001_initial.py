# Generated by Django 4.1.5 on 2023-03-12 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=60, verbose_name='Cargo')),
            ],
            options={
                'ordering': ['cargo'],
            },
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre Empleado')),
                ('tdoc', models.CharField(choices=[('CC', 'CC'), ('PEP', 'PEP'), ('PPT', 'PPT'), ('TI', 'TI')], default='CC', max_length=10, verbose_name='Tipo De Documento')),
                ('cedula', models.IntegerField(verbose_name='Cedula Empleado')),
                ('empresa', models.CharField(choices=[('Heavens Fruits SAS', 'Heavens Fruits SAS'), ('People', 'People')], default='Heavens Fruits SAS', max_length=100, verbose_name='Empresa')),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10, verbose_name='Estado')),
                ('contrato', models.CharField(choices=[('Aprendizaje', 'Aprendizaje'), ('Fijo', 'Fijo'), ('Indefinido', 'Indefinido'), ('Labor Contrada', 'Labor Contrada'), ('Obra Labor', 'Obra Labor')], default='Indefinido', max_length=20, verbose_name='Contrato')),
                ('area', models.CharField(choices=[('Administracion', 'Administracion'), ('Compras', 'Compras'), ('Comercial', 'Comercial'), ('Exportaciones', 'Exportaciones'), ('Gestion TI', 'Gestion TI'), ('Logistica', 'Logistica'), ('Operaciones', 'Operaciones')], max_length=33, verbose_name='Area')),
                ('salario', models.IntegerField(verbose_name='Salario')),
                ('generaextras', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], default='No', max_length=2, verbose_name='Genera Extras')),
                ('ingreso', models.DateField(max_length=10, null=True, verbose_name='Fecha Ingreso')),
                ('retiro', models.DateField(blank=True, max_length=10, null=True, verbose_name='Fecha Retiro')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.cargos', verbose_name='Cargo')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio_jornada_global', models.DateTimeField(null=True, verbose_name='Inicio Jornada')),
                ('salida_jornada_global', models.DateTimeField(null=True, verbose_name='Salida Jornada')),
                ('inicio_descanso_global', models.DateTimeField(blank=True, null=True, verbose_name='Inicio Descanso')),
                ('salida_descanso_global', models.DateTimeField(blank=True, null=True, verbose_name='Salida Descanso')),
                ('inicio_descanso_global2', models.DateTimeField(blank=True, null=True, verbose_name='Inicio Descanso 2')),
                ('salida_descanso_global2', models.DateTimeField(blank=True, null=True, verbose_name='Salida Descanso 2')),
                ('jornada_legal', models.IntegerField(default=8, verbose_name='Jornada Legal')),
                ('fh_transaccion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha De Transacción')),
                ('total_horas', models.FloatField(default=0, verbose_name='Total Horas')),
                ('diurnas_totales', models.FloatField(default=0, verbose_name='Horas Diurnas')),
                ('nocturnas_totales', models.FloatField(default=0, verbose_name='Horas Nocturnas')),
                ('extras_diurnas_totales', models.FloatField(default=0, verbose_name='Horas Extras Diurnas')),
                ('extras_nocturnos_totales', models.FloatField(default=0, verbose_name=' Horas Extras Nocturnas')),
                ('diurnos_festivo_totales', models.FloatField(default=0, verbose_name='Horas Diurnas Festivas')),
                ('nocturnos_festivo_totales', models.FloatField(default=0, verbose_name='Horas Nocturnas Festivas')),
                ('extras_diurnos_festivo_totales', models.FloatField(default=0, verbose_name='Horas Extras Diurnas Festivas')),
                ('extras_nocturnos_festivo_totales', models.FloatField(default=0, verbose_name='Horas Extras Nocturnas Festivas')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.empleados')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creada Por')),
            ],
            options={
                'ordering': ['empleado'],
            },
        ),
    ]
