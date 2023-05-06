from rest_framework import generics
from .models import Account
from .serializers import RegisterSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOnGetRoute, IsAdminOrCritic


class AccountView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOnGetRoute]

    queryset = Account.objects.all()
    serializer_class = RegisterSerializer


class AccountUpdateView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrCritic]

    queryset = Account.objects.all()
    serializer_class = RegisterSerializer
    lookup_url_kwarg = "user_id"
