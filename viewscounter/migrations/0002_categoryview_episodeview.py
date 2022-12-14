# Generated by Django 3.2.3 on 2021-06-09 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewscounter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryView',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EpisodeView',
            fields=[
                ('episode', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
    ]
