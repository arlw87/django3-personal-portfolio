# Generated by Django 3.1.1 on 2020-09-14 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('date', models.DateField(auto_now_add=True)),
                ('blogContent', models.TextField()),
            ],
        ),
    ]