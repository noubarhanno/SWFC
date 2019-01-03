from django.db import models
from django.urls import reverse,reverse_lazy
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Registration(models.Model):
    First_Name = models.CharField(max_length=256)
    Last_Name = models.CharField(max_length=256)
    Email_Address = models.CharField(max_length=256)
    Mobile_Number = models.IntegerField()
    Intereset = models.CharField(max_length=1000)

    def __Str__(self):
        return self.First_Name

    def get_absolute_url(self):
            return reverse_lazy('Index_View')
