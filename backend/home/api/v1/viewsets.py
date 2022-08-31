from rest_framework import viewsets
from home.models import Abhjiy231, Abhjjjhg, Devtest123
from .serializers import Abhjiy231Serializer, AbhjjjhgSerializer, Devtest123Serializer
from rest_framework import authentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from home.api.v1.serializers import (
    SignupSerializer,
    UserSerializer,
)


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class AbhjjjhgViewSet(viewsets.ModelViewSet):
    serializer_class = AbhjjjhgSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Abhjjjhg.objects.all()


class Devtest123ViewSet(viewsets.ModelViewSet):
    serializer_class = Devtest123Serializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Devtest123.objects.all()


class Abhjiy231ViewSet(viewsets.ModelViewSet):
    serializer_class = Abhjiy231Serializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Abhjiy231.objects.all()
