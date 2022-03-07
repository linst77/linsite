# Generated by Django 4.0.3 on 2022-03-06 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FileModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, null=True, upload_to='media/%Y%m%d/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_customer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-user'],
            },
        ),
        migrations.CreateModel(
            name='MoTestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father', models.CharField(blank=True, max_length=200)),
                ('mother', models.CharField(blank=True, max_length=200)),
                ('baby', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=200)),
                ('event_date', models.DateTimeField()),
                ('content_first', models.CharField(blank=True, max_length=200)),
                ('content_sec', models.CharField(blank=True, max_length=200)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=200, null=True, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('photo_first', models.ManyToManyField(blank=True, related_name='photo_first', to='motest.filemodels')),
                ('photo_sec', models.ManyToManyField(blank=True, related_name='photo_sec', to='motest.filemodels')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-user'],
            },
        ),
    ]
