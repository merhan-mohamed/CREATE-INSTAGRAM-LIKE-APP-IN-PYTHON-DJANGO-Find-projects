from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django_mysql.models import query

from rest_framework import generics, status
from rest_framework.response import Response
import Insta
from Insta import settings as Insta_settings, models
from Insta.auth import settings, serializers
from Insta.auth.serializers import LogoutSerializer, LoginSerializer, RegisterSerializer
from Insta.auth.utils import AuthTools
from Insta.models import Profile
from Insta.serializer import user
from Insta.serializer.profile import ProfileSerializer
from Insta.serializer.user import UserSerializer



class UserView(generics.RetrieveUpdateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = Insta_settings.CONSUMER_PERMISSIONS

    def get_object(self,*args,**kwargs):
        return self.request.user

class ProfileView(generics.RetrieveUpdateAPIView):
    model = User.profile
    serializer_class = ProfileSerializer
    permission_classes = Insta_settings.CONSUMER_PERMISSIONS

    def get_object(self,*args,**kwargs):
        return self.request.profile

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = Insta_settings.UNPROTECTED

    def post(self,request):
        if 'email' in request.data and 'password' in request.data:
            email = request.data['email'].lower()
            password = request.data['password']
            user = AuthTools.authenticate_email(email, password)
            if user is not None and AuthTools.login(request, user):
                token = AuthTools.issue_user_token(user, 'login')
                serializer = serializers.LoginCompleteSerializer(token)
                return Response(serializer.data)

        message = {'message': 'Unable to login with the credentials provided'}
        return Response(message, status = status.HTTP_400_BAD_REQUEST)

class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = Insta_settings.CONSUMER_PERMISSIONS

    def post(self,request):
        if AuthTools.logout(request):
            data = {'logout':'success'}
            return Response(data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = Insta_settings.UNPROTECTED

    def perform_create(self, serializer):
        serializer.save()



