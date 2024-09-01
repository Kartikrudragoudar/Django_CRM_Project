from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=20)
    email_address = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")