from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import UserViewSet


urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', UserViewSet.as_view({'get': 'list',
                                           'post': 'create'}))
]