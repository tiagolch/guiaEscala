# Generated by Django 3.2.6 on 2021-08-18 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcao', models.CharField(max_length=50, verbose_name='Ministério')),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Funcoes',
            },
        ),
        migrations.CreateModel(
            name='Ministerio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Ministério')),
                ('ativo', models.BooleanField(default=True)),
                ('funcao', models.ManyToManyField(to='ministerio.Funcao', verbose_name='Função')),
            ],
            options={
                'verbose_name_plural': 'Ministerios',
            },
        ),
    ]
