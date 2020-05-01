from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from Insta.auth.utils import AuthTools




class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()


class LoginCompleteSerializer(serializers.Serializer):
    auth_token = serializers.CharField(source='key', read_only=True)

class LogoutSerializer(serializers.Serializer):
    pass

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User.USERNAME_FIELD,
            'email',
            'first_name',
            'last_name',
            'password',
        )
        write_only_fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )

    def save(self, **kwargs):
        data = self.init_data if hasattr(self, 'init_data') else self.initial_data
        items = dict(data.items())
        user_data = {
            'username': items['username'],
            'email': items['email'],
            'password': items['password'],
            'first_name': items['first_name'],
            'last_name': items['last_name'],
        }

        profile_data = {
             'role': 'consumer',
        }

        group = profile_data['role'] + '_basic'
        user = AuthTools.register(user_data, profile_data, group)
        if user is not None:
            self.object = user
            return self.object

        raise serializers.ValidationError('Unable to register with the credentials provided.')



