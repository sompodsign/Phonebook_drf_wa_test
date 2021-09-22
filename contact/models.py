from django.db import models


# Create your models here.
class Contact(models.Model):
    contact_name = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.contact_name
