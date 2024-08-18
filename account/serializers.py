import sentry_sdk
import requests
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import APIException


from account.auth import google, register, facebook
from django.conf import settings
from common.serializers import MediaURlSerializer


from account.models import SocialUser, User, UserMessage


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")


class UserOtpCodeVerifySerializer(serializers.Serializer):
    code = serializers.IntegerField(required=True)  # todo: add validation
    email = serializers.EmailField(required=True)


class GoogleSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        
        token_url = 'https://oauth2.googleapis.com/token'
        payload = {
            'code': auth_token,
            'client_id': settings.GOOGLE_CLIENT_ID,
            'client_secret': settings.GOOGLE_CLIENT_SECRET,
            'redirect_uri': settings.GOOGLE_REDIRECT_URI,
            'grant_type': settings.GOOGLE_GRANT_TYPE,
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(token_url, data=payload, headers=headers)


        if response.status_code == 200:
            id_token_str = response.json()['id_token'] 
            user_data = google.Google.validated(id_token_str)

        else:
            raise Exception(f'Error fetching token: {response.json()}')

        if not auth_token:
            raise APIException('Код авторизации отсутствует')
        if not user_data:
            raise APIException('Ошибка верификации токена Google')



        email = user_data.get("email")
        first_name = user_data.get("given_name", "")
        last_name = user_data.get("family_name", "")
        photo = user_data.get("picture", None)
        birthday = user_data.get("birthday", None)
        username = first_name + last_name

        try:
            return register.register_social_user(
                auth_type=User.AuthType.GOOGLE,
                email=email,
                first_name=first_name,
                last_name=last_name,
                birthday=birthday,
                username=username,
                photo=photo,
            )
        except Exception as e:
            raise serializers.ValidationError(f'Ошибка при регистрации пользователя: {e}')
        

class FacebookSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = facebook.Facebook.validated(auth_token=auth_token)

        email = user_data.get("email")
        first_name = user_data.get("given_name", "")
        last_name = user_data.get("family_name", "")
        photo = user_data.get("picture", None)
        birthday = user_data.get("birthday", None)
        username = first_name + last_name

        try:
            return register.register_social_user(
                auth_type=User.AuthType.FACEBOOK,
                email=email,
                first_name=first_name,
                last_name=last_name,
                birthday=birthday,
                username=username,
                photo=photo,
            )
        except Exception as e:
            raise serializers.ValidationError(f'Ошибка при регистрации пользователя: {e}')
        

class UserSerializer(serializers.ModelSerializer):
    photo = MediaURlSerializer(read_only=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "photo", "birth_date")




class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessage
        fields = '__all__'
