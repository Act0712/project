# Generated by Django 4.0.7 on 2022-09-07 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing', '0002_remove_manufacturing_process_final'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturing_process',
            name='final',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
