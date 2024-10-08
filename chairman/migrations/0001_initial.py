# Generated by Django 5.0.7 on 2024-09-30 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('charges_type', models.CharField(max_length=100)),
                ('member_name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('inv', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('discription', models.TextField()),
            ],
        ),
    ]
