# Generated by Django 4.0.3 on 2022-03-06 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motest', '0002_alter_motestmodel_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motestmodel',
            name='event_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
