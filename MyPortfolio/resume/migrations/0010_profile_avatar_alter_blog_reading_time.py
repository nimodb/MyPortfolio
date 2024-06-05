# Generated by Django 5.0.6 on 2024-06-05 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_blog_reading_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='reading_time',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
