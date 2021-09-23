from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('contact/<str:pk>/', views.get_contact, name='contact'),
    path('contact/create-contact/', views.create_contact, name='create')
]
