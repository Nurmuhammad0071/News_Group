# Generated by Django 4.2.9 on 2024-01-17 12:12

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('noactive', 'NoActive')], max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Yangliklar',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
