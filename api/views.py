from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContactSerializer
from .models import Contact


# Create your views here.
# @api_view(['GET', 'POST'])
def get_contacts(request):
    qs = Contact.objects.all().order_by('contact_name')
    serializer = ContactSerializer(qs, many=True)
    return Response(serializer.data)
