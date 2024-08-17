from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserRegisterVerifyView, UserRegisterView, GoogleAuth, FacebookAuth

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("register/verify/", UserRegisterVerifyView.as_view(), name="register-verify"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('google/', GoogleAuth.as_view(), name='googleauth'),
    path('facebook/', FacebookAuth.as_view(), name='facebookauth'),
]
