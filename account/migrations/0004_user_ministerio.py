# Generated by Django 3.2.6 on 2021-10-10 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0003_auto_20210910_1114'),
        ('account', '0003_user_funcao'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ministerio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='ministerio.ministerio'),
            preserve_default=False,
        ),
    ]
