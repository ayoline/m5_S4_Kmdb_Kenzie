from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from .views import AccountView, AccountUpdateView

urlpatterns = [
    path("users/", AccountView.as_view()),
    path("users/login/", ObtainAuthToken.as_view()),
    path("users/register/", AccountView.as_view()),
    path("users/<int:user_id>/", AccountUpdateView.as_view()),
]
