# Generated by Django 2.2.5 on 2021-09-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedday',
            name='created',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='bookedday',
            name='updated',
            field=models.DateTimeField(default=''),
        ),
    ]
