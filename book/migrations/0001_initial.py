# Generated by Django 3.2 on 2022-05-23 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
                ('numPages', models.IntegerField()),
            ],
        ),
    ]