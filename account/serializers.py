from rest_framework import serializers

from account.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")


class UserOtpCodeVerifySerializer(serializers.Serializer):
    code = serializers.IntegerField(required=True)  # todo: add validation
    email = serializers.EmailField(required=True)
