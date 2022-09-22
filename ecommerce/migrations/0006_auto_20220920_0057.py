# Generated by Django 3.2 on 2022-09-20 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_ciudad'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='flag_unidadmedida',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad_medida',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
