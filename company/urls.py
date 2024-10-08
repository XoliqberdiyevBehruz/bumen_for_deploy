from django.urls import path

from .views import *

urlpatterns = [
    path("contact_with_us/", ContactWithUsView.as_view(), name="contact_with_us"),
    path("faqs/", FAQAPIView.as_view(), name="faqs"),
    path('contact/', ContactsDetailView.as_view(), name="contact")
]
