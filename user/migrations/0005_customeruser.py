# Generated by Django 5.1.1 on 2024-09-17 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_customer_customer_creationtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuser_name', models.CharField(max_length=50)),
                ('cuser_creationTime', models.DateTimeField(auto_now_add=True)),
                ('cuser_superuser', models.BooleanField(default=False)),
            ],
        ),
    ]
