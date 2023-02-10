# Generated by Django 3.2.15 on 2023-02-09 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0006_auto_20220920_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('f_creacion', models.DateTimeField(auto_now_add=True)),
                ('f_modificacion', models.DateTimeField(auto_now=True)),
                ('user_updated', models.IntegerField(blank=True, null=True)),
                ('pcorr1', models.IntegerField()),
                ('pcorr2', models.IntegerField()),
                ('pnum1', models.IntegerField(blank=True, null=True)),
                ('pnum2', models.IntegerField(blank=True, null=True)),
                ('pdesc', models.CharField(blank=True, max_length=1000, null=True)),
                ('ptxt1', models.CharField(blank=True, max_length=1000, null=True)),
                ('ptxt2', models.CharField(blank=True, max_length=1000, null=True)),
                ('pclob1', models.TextField(blank=True, null=True)),
                ('pclob2', models.TextField(blank=True, null=True)),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
