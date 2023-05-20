# Generated by Django 4.0.7 on 2022-08-30 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quality_model1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phonenumber', models.PositiveBigIntegerField(null=True)),
                ('gender', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
