# Generated by Django 5.0.6 on 2024-05-24 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
