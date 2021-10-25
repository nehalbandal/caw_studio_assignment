from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie, MovieSchedule, Booking
from rest_framework.response import Response

from .serializers import *


class RegistrationAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginAPI(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = request.data.get('username')
            password = request.data.get('password')
            if User.objects.filter(username=username, password=password).count():
                serializer = UserSerializer(User.objects.filter(username=username, password=password).first())
                data = serializer.data
                status = True
                message = "Success"
            else:
                data = None
                status = False
                message = "Failure"
        else:
            data = None
            status = False
            message = serializer.errors

        return Response({
            "status": status,
            "message": message,
            "data": data
        })


class MoviesListAPI(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name',]
    search_fields = ['^name', ]


class MovieScheduleListAPI(ListAPIView):
    queryset = MovieSchedule.objects.all()
    serializer_class = MovieScheduleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['movie__name', 'theater__name', 'theater__city']
    search_fields = ['^theater__city', '^movie__name', '^theater__name']


class TicketBookingAPI(CreateAPIView):
    """
        API to book movie ticket

        ### Note
            Pass authorization token in header
            Ex. "Authorization": "Token c740055ff2313ebdbb393da3cb2b0e23dd02a34d"
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
