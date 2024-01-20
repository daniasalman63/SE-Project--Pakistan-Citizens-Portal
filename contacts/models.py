from django.db import models

class Contact(models.Model):
    contact_name = models.CharField(max_length=200)
    contact_email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    contact_phone = models.CharField(max_length=12)
