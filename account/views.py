from datetime import timedelta

from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, UserOtpCode
from .serializers import (
    GoogleSerializer,
    FacebookSerializer,
    UserOtpCodeVerifySerializer,
    UserRegisterSerializer,
)
from .utils import generate_otp_code, send_verification_code


class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=False)
        user.set_password(serializer.validated_data["password"])
        user.save()
        code = generate_otp_code()
        new_otp_code = UserOtpCode.objects.create(
            user=user,
            code=code,
            type=UserOtpCode.VerificationType.REGISTER,
            expires_in=timezone.now()
            + timedelta(minutes=settings.OTP_CODE_VERIFICATION_TIME),
        )
        send_verification_code(user.email, new_otp_code.code)


class UserRegisterVerifyView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserOtpCodeVerifySerializer

    def create(self, request, *args, **kwargs):
        try:

            data = self.serializer_class(data=request.data)
            if not data.is_valid():
                return Response(
                    status=status.HTTP_400_BAD_REQUEST, data={"message": "Invalid data"}
                )
            user = User.objects.get(email=data.data["email"])
            user_otp_code = UserOtpCode.objects.filter(
                user=user, code=data.data["code"], is_used=False
            )
            if not user_otp_code.exists():
                return Response(
                    status=status.HTTP_404_NOT_FOUND,
                    data={"message": "otp code not found"},
                )
            user_otp_code = user_otp_code.filter(expires_in__gte=timezone.now())
            if not user_otp_code.exists():
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={"message": "otp code was expired"},
                )

            user.is_active = True
            user.save()
            otp_code = user_otp_code.first()
            otp_code.is_used = True
            otp_code.save()
            return Response(
                status=status.HTTP_200_OK, data={"message": "user is activated"}
            )
        except User.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"message": "User does not exist"},
            )


class GoogleAuth(APIView):
    def get(self, request, *args, **kwargs):
        auth_token = str(request.query_params.get('code'))
        ser = GoogleSerializer(data={'auth_token': auth_token})
        if ser.is_valid():
            return Response(ser.data)
        return Response(ser.errors, status=400)
 

class FacebookAuth(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = FacebookSerializer
    
