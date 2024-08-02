import sentry_sdk
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from account.auth import google, register
from account.models import SocialUser, User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")


class UserOtpCodeVerifySerializer(serializers.Serializer):
    code = serializers.IntegerField(required=True)  # todo: add validation
    email = serializers.EmailField(required=True)


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        try:
            user_data = google.Google.validate(auth_token)
            try:
                user_data["sub"]
            except Exception:
                sentry_sdk.capture_exception(user_data)
                raise serializers.ValidationError(
                    _("The token is invalid or expired. Please login again.")
                )

            user_id = user_data["sub"]
            email = user_data["email"]
            provider = SocialUser.RegisterType.GOOGLE
            first_name = (
                user_data["given_name"]
                if "given_name" in user_data
                else user_data["email"]
            )
            last_name = user_data["family_name"] if "family_name" in user_data else ""
            return register.register_social_user(
                provider=provider,
                user_id=user_id,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )
        except Exception as e:
            sentry_sdk.capture_exception(e)
            raise serializers.ValidationError(e)
