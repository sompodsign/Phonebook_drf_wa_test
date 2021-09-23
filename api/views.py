from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContactSerializer
from .models import Contact


# Create your views here.
@api_view(['GET'])
def get_contact(request, id):
    qs = Contact.objects.get(id)
    serializer = ContactSerializer(qs, many=True)
    return Response(serializer.data)
