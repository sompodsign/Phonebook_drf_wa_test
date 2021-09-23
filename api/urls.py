from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('contact/<str:id>/', views.get_contact, name='api')
]
