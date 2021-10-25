# Generated by Django 3.2.8 on 2021-10-25 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_booking_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieschedule',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_schedule', to='movies.movie'),
        ),
        migrations.AlterField(
            model_name='movieschedule',
            name='theater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theater_schedule', to='movies.theater'),
        ),
    ]
