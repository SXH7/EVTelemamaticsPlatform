# Generated by Django 5.0.2 on 2024-07-20 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_device_device_chemistry_alter_device_device_current_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='id',
        ),
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_voltage',
            field=models.IntegerField(choices=[(400, '400V'), (500, '500V'), (600, '600V')], null=True),
        ),
    ]
