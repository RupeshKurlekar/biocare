# Generated by Django 3.2 on 2021-05-05 13:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('technician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PT_ID', models.CharField(max_length=255)),
                ('PT_REG_NO', models.CharField(max_length=255)),
                ('PT_NAME', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Please enter valid name', regex='^[a-zA-Z ]+$')])),
                ('PT_GENDER', models.CharField(max_length=20)),
                ('PT_AGE', models.CharField(max_length=255)),
                ('PT_MOB', models.CharField(max_length=255)),
                ('TIME', models.DateTimeField(auto_now=True)),
                ('TECHNICIAN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technician.technician')),
            ],
            options={
                'db_table': 'Patient',
            },
        ),
        migrations.CreateModel(
            name='PatientHistoryFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PT_HSTY_FILE_ID', models.CharField(max_length=255)),
                ('PT_HSTY_FILE', models.ImageField(max_length=255, upload_to='patient_history_files')),
                ('TIME', models.DateTimeField(auto_now=True)),
                ('PT_HSTY_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
            options={
                'db_table': 'Patient History Files',
            },
        ),
        migrations.CreateModel(
            name='PatientHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PT_HSTY_ID', models.CharField(max_length=255)),
                ('IS_SENT', models.IntegerField(default=0)),
                ('RP_REMARKS', models.TextField(max_length=255)),
                ('TIME', models.DateTimeField(auto_now=True)),
                ('PATIENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
            options={
                'db_table': 'Patient History',
            },
        ),
    ]
