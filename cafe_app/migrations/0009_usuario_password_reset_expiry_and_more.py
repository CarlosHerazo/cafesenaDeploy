# Generated by Django 5.0.6 on 2024-06-07 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe_app', '0008_venta_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='password_reset_expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password_reset_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
