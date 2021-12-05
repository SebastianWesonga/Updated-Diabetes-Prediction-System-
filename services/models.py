from django.db import models
from django.conf import settings

# Create your models here.
class Service(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE)
    pregnacies =models.DecimalField(max_digits=10, decimal_places=0,
            blank=True, null=True)
    glucose = models.CharField(max_length = 200)
    blood_pressure = models.CharField(max_length = 200)
    skin_thickness = models.CharField(max_length = 200)
    insulin = models.CharField(max_length = 200)
    bmi = models.CharField(max_length = 200)
    diabetes_pedigree = models.CharField(max_length = 200)
    age = models.DecimalField(max_digits=3, decimal_places=0)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Service for user {self.user.username}'

