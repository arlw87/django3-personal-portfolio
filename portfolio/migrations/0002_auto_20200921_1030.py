# Generated by Django 3.1.1 on 2020-09-21 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioproject',
            name='description',
            field=models.CharField(max_length=400),
        ),
    ]