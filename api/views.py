from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContactSerializer
from .models import Contact


# Create your views here.
@api_view(['GET'])
def get_contact(request, pk):
    contact_obj = Contact.objects.get(id=pk)
    serializer = ContactSerializer(contact_obj, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_contact(request):
    pass
