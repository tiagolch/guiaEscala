# Generated by Django 3.2.6 on 2021-08-18 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0002_alter_funcao_funcao'),
        ('account', '0002_remove_user_funcao'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='funcao',
            field=models.ManyToManyField(to='ministerio.Funcao'),
        ),
    ]
