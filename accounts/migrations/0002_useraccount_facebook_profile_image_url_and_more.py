# Generated by Django 5.0.4 on 2024-04-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='facebook_profile_image_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='google_profile_image_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
