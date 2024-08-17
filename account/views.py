from datetime import timedelta

from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .permissions import IsGroupMember

from .models import User, UserOtpCode, UserMessage, Groups
from .serializers import (
    GoogleSocialAuthSerializer,
    UserOtpCodeVerifySerializer,
    UserRegisterSerializer,
    UserMessageSerializer
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


class GoogleRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = GoogleSocialAuthSerializer



class UserMessageCreateApi(CreateAPIView):
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsGroupMember]

    def perform_create(self, serializer):
        group = serializer.validated_data['group']
        if self.request.user not in group.users.all():
            raise PermissionDenied("You are not a member of this group.")
        serializer.save(user=self.request.user)

class MessageListApi(ListAPIView):
    serializer_class = UserMessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsGroupMember]

    def get_queryset(self):
        group_id = self.kwargs['group_id']
        group = Groups.objects.get(pk=group_id)
        if self.request.user not in group.users.all():
            raise PermissionDenied("You are not a member of this group.")
        return UserMessage.objects.filter(group=group)