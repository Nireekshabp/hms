# Generated by Django 4.0.5 on 2023-10-21 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ward', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('patient_id', models.CharField(blank=True, max_length=8, unique=True)),
                ('dob', models.DateField()),
                ('contact_number', models.CharField(max_length=12)),
                ('admission_date', models.DateField()),
                ('is_discharged', models.BooleanField(default=False)),
                ('ward_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_user', to='ward.ward')),
            ],
        ),
    ]