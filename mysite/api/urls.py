from django.urls import path, include
# from .Serializers import
from rest_framework import routers
from .views import UserViewSet, GroupViewSet


app_name = 'api'
urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    path('users/', UserViewSet.as_view(), name='users'),
    path('groups/', GroupViewSet.as_view(), name='groups'),
]
