# Generated by Django 4.2.9 on 2024-01-17 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tite', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to=None)),
                ('data', models.DateField()),
                ('text', models.TextField()),
            ],
        ),
    ]
