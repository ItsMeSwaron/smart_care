# Generated by Django 5.1.3 on 2025-03-01 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0003_review'),
        ('patient', '0002_alter_patient_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_types', models.CharField(max_length=10, verbose_name=[('Offline', 'Offline'), ('Online', 'Online')])),
                ('appointment_status', models.CharField(default='Pending', max_length=10, verbose_name=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Running', 'Running')])),
                ('symptom', models.TextField()),
                ('cancel', models.BooleanField(verbose_name=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('time', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.availabletime')),
            ],
        ),
    ]
