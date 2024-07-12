from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from company.models import ContactWithUs
from company.serializers import ContactWithUsSerializer


class ContactWithUsView(CreateAPIView):
    queryset = ContactWithUs.objects.all()
    serializer_class = ContactWithUsSerializer

