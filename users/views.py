from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import (
    LoginSerializer, ApiUserSerializer)


@swagger_auto_schema(methods=['post'], request_body=LoginSerializer)
@api_view(["POST"])
def login(request):
    if request.method == "POST":
        data = {}
        try:
            data = request.data
        except:
            return Response({"error": "data key must be provided"}, status=status.HTTP_400_BAD_REQUEST)
        if not isinstance(data, dict):
            return Response({"error": "data must be object"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data["email"], password=serializer.validated_data["password"])
            userData = ApiUserSerializer(user)
            if user:
                return Response({
                    "user": userData.data,
                    "tokens": user.tokens(),
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "wrong credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)