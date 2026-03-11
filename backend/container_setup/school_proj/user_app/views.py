from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.status as s
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class Sign_Up(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        try:
            user = User.objects.create_user(
                username=request.data.get('email'),
                email=request.data.get('email'),
                password=request.data.get('password')
            )
            token = Token.objects.create(user=user)
            login(request, user)
            return Response(
                {"Username": user.email, "token": token.key}, status=s.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                f"Unable to create user with {user_data}\n" + str(e), status=s.HTTP_400_BAD_REQUEST
            )

class Log_In(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(username=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "User": user.email}, status=s.HTTP_200_OK)
        else:
            return Response("No trainer matching credentials", status=s.HTTP_404_NOT_FOUND)
        
class Info(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"email": request.user.email})

class Log_Out(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=s.HTTP_204_NO_CONTENT)