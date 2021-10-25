from django.conf.urls import url
from django.urls import path
from . import api
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Movies API",
      default_version='v1',
      description="Test description",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('register/', api.RegistrationAPI.as_view(), name="register"),
    path('login/', api.LoginAPI.as_view(), name="login"),
    path('movies/', api.MoviesListAPI.as_view(), name="movies-list"),
    path('movie-schedules/', api.MovieScheduleListAPI.as_view(), name="movie-schedule-list"),
    path('ticket-booking/', api.TicketBookingAPI.as_view(), name="booking"),
]