# Generated by Django 5.0.6 on 2024-05-23 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_remove_profile_cv_profile_cv_de_profile_cv_en'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=50)),
            ],
        ),
    ]
