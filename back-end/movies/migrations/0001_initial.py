# Generated by Django 3.2.3 on 2021-11-17 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('vote', models.FloatField()),
                ('country', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=10)),
                ('grade', models.CharField(max_length=10)),
                ('poster_path', models.TextField()),
                ('genre_1', models.CharField(max_length=10)),
                ('genre_2', models.CharField(default='', max_length=10)),
                ('genre_3', models.CharField(default='', max_length=10)),
                ('genre_4', models.CharField(default='', max_length=10)),
                ('actor_1', models.CharField(max_length=20)),
                ('actor_2', models.CharField(default='', max_length=20)),
                ('actor_3', models.CharField(default='', max_length=20)),
                ('content', models.TextField()),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('day', models.IntegerField(default='')),
            ],
        ),
    ]