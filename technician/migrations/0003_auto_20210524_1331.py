# Generated by Django 3.1 on 2021-05-24 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technician', '0002_technician_tech_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technician',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='technicianlogin',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
