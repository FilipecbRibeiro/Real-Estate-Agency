# Generated by Django 3.0.5 on 2020-05-08 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
