# Generated by Django 5.0.4 on 2024-05-01 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radiology', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Link', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=500)),
                ('DoctorName', models.CharField(max_length=500)),
                ('City', models.CharField(max_length=500)),
                ('Location', models.CharField(max_length=500)),
                ('Specialiter', models.CharField(max_length=500)),
            ],
        ),
    ]