# Generated by Django 4.0.5 on 2022-08-14 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_database_movie_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='movie_poster',
            field=models.ImageField(default='default.jpg ', upload_to='video_photoes'),
        ),
    ]
