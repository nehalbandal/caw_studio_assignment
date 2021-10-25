from django.contrib.auth.models import User
from rest_framework import serializers

from movies.models import Movie, MovieSchedule, Booking, Theater


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=300)
    password = serializers.CharField(max_length=300)


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = "__all__"

    def get_token(self, obj):
        return obj.auth_token.key


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class TheaterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theater
        exclude = ['id',]


class MovieScheduleSerializer(serializers.ModelSerializer):
    theater = TheaterSerializer()
    available_seats = serializers.SerializerMethodField(default=0)

    class Meta:
        model = MovieSchedule
        fields = "__all__"
        depth = 1

    def get_available_seats(self, obj):
        return obj.theater.total_seats - obj.bookings.count()


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

    def validate(self, data):
        obj = data['schedule']
        diff = obj.theater.total_seats - obj.bookings.count()
        if diff == 0:
            raise serializers.ValidationError("No seats available.")
        return data