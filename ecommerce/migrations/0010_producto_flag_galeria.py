# Generated by Django 3.1.14 on 2023-04-04 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0009_auto_20230403_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='flag_galeria',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]