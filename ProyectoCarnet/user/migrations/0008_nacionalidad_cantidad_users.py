# Generated by Django 3.1 on 2020-09-28 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_nacionalidad_cantidad_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='nacionalidad',
            name='cantidad_users',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]