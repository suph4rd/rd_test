# Generated by Django 3.1.4 on 2020-12-16 19:18

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
            name='Employes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=255, verbose_name='Отчество')),
                ('date_employ', models.DateField(auto_now=True, verbose_name='Дата приёма на работу')),
                ('salary', models.FloatField(verbose_name='Заработная плата')),
            ],
            options={
                'verbose_name': 'Работники',
                'verbose_name_plural': 'Работники',
            },
        ),
        migrations.CreateModel(
            name='Salary_paid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_paid', models.DateField()),
                ('sum_paid', models.FloatField()),
                ('emploee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employes')),
            ],
            options={
                'verbose_name': 'Заработная плата',
                'verbose_name_plural': 'Заработная плата',
            },
        ),
        migrations.CreateModel(
            name='Position_relations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255, unique=True, verbose_name='Должность')),
                ('level', models.SmallIntegerField(verbose_name='Уровень должности')),
                ('chief', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.position_relations', verbose_name='Начальник')),
            ],
            options={
                'verbose_name': 'Cвязь начальник и подчинённый',
                'verbose_name_plural': 'Cвязь начальников и подчинённых',
            },
        ),
        migrations.AddField(
            model_name='employes',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.position_relations', verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='employes',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
