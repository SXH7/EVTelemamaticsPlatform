# Generated by Django 5.0.2 on 2024-07-19 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='device_chemistry',
            field=models.CharField(choices=[('Lithium Ion', 'Lithium Ion'), ('Lead Acid', 'Lead Acid'), ('NCA', 'NCA'), ('NMC', 'NMC')], null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_current',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_voltage',
            field=models.IntegerField(choices=[(400, '400V'), (500, '500V'), (600, '500V')], null=True),
        ),
    ]
