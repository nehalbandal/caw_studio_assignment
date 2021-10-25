import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Movie(models.Model):
    name = models.CharField(max_length=300)
    length = models.TimeField(default=datetime.time(2, 30, 00))

    def __str__(self):
        return self.name


class Theater(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    total_seats = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.city, self.name)


class MovieSchedule(models.Model):
    movie = models.ForeignKey(Movie, related_name="movie_schedule", on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, related_name="theater_schedule", on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ticket_price = models.PositiveIntegerField(default=50)

    def __str__(self):
        return "{} - {} - {} to {}".format(self.movie, self.theater, self.start_time, self.end_time)


class Booking(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    schedule = models.ForeignKey(MovieSchedule, related_name="bookings", on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)