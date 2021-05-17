from django.db import models

class CustomerInfo(models.Model):
    branding = models.BooleanField()
    marketing = models.BooleanField()
    design = models.BooleanField()
    name = models.CharField(max_length=256)
    email = models.EmailField()
    phonenumber = models.PositiveIntegerField()
    tellus = models.TextField()

    def __str__(self):
        return self.name
