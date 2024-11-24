# Generated by Django 5.1.3 on 2024-11-21 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='gallary')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('cat', models.CharField(max_length=200)),
                ('client', models.CharField(max_length=200)),
                ('project_date', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.category')),
                ('image_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.agents')),
            ],
        ),
    ]