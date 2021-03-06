# Generated by Django 3.2 on 2021-05-06 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radiologist', '0002_alter_radiologistpmt_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiologist',
            name='RDLG_ID',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radiologist',
            name='RDLG_REG_NO',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radiologistpmt',
            name='RDLG_PMT_ID',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radiologistreportfiles',
            name='RDLG_RPT_FILE_ID',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radiologistreportmap',
            name='RDLG_RPT_ID',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
