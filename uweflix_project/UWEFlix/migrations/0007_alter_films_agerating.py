# Generated by Django 4.1.5 on 2023-01-12 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UWEFlix', '0006_alter_films_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='ageRating',
            field=models.CharField(choices=[('U', 'U'), ('PG', 'PG'), ('12A', '12A'), ('15', '15'), ('18', '18'), ('R18', 'R18')], default='green', max_length=50),
        ),
    ]
