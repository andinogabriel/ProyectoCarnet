# Generated by Django 3.1 on 2020-09-15 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCarnet', '0001_initial'),
        ('user', '0002_auto_20200915_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppCarnet.direcciones'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='grupo_s',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppCarnet.gruposanguineo'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nacionalidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppCarnet.nacionalidad'),
        ),
    ]
