# Generated by Django 4.0.5 on 2022-08-14 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Horror', 'Horror'), ('Western', 'Western'), ('Romance', 'Romance'), ('Adventure', 'Adventure'), ('Music', 'Music')], max_length=10),
        ),
    ]
