from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (GoogleRegisterView, UserRegisterVerifyView, UserRegisterView, UserMessageCreateApi, MessageListApi)

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("register/verify/", UserRegisterVerifyView.as_view(), name="register-verify"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/google/", GoogleRegisterView.as_view(), name="google_register"),
    path('messages/', UserMessageCreateApi.as_view(), name='create_message'),
    path('messages/<int:group_id>/', MessageListApi.as_view(), name='list_messages'),
]

