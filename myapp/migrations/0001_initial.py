# Generated by Django 5.0.4 on 2024-04-24 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('keywords', models.CharField(max_length=100)),
                ('instaurl', models.CharField(max_length=300)),
                ('fburl', models.CharField(max_length=300)),
                ('linkedinurl', models.CharField(max_length=300)),
                ('githuburl', models.CharField(max_length=300)),
                ('xurl', models.CharField(max_length=300)),
            ],
        ),
    ]
