# Generated by Django 5.0.6 on 2024-05-27 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_alter_blog_options_blog_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='reading_time',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
