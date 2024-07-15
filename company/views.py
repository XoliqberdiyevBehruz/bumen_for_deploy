from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from company.models import ContactWithUs, FAQ
from company.serializers import ContactWithUsSerializer, FAQSerializer


class ContactWithUsView(CreateAPIView):
    queryset = ContactWithUs.objects.all()
    serializer_class = ContactWithUsSerializer


class FAQAPIView(APIView):
    serializer_class = FAQSerializer

    def get(self, request, *args, **kwargs):
        try:
            queryset = FAQ.objects.all()
            serializer = FAQSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception:
            return Response(data={"message": "Internal Server Error"}, status=500)
