# Generated by Django 4.2.20 on 2025-05-18 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_admission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField(max_length=8)),
                ('gender', models.CharField(max_length=4)),
                ('current_class', models.CharField(max_length=2)),
            ],
        ),
    ]
