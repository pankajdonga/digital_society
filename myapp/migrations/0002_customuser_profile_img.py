# Generated by Django 5.0.7 on 2024-09-26 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='profile_img'),
        ),
    ]
