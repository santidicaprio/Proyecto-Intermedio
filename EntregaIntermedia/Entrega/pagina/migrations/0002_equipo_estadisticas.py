# Generated by Django 4.0.5 on 2022-07-16 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='estadisticas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goles', models.CharField(max_length=80)),
                ('asistencias', models.IntegerField()),
            ],
        ),
    ]
