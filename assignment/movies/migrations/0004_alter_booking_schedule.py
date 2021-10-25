# Generated by Django 3.2.8 on 2021-10-25 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movieschedule_ticket_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='movies.movieschedule'),
        ),
    ]
