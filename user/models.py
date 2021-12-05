from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE, related_name='user_profile')
    photo = models.ImageField(upload_to='patients/%Y/%m/%d/', blank=True,
            null=True)
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
            (MALE,  'Male'),
            (FEMALE, 'Female')
            ]
    gender = models.CharField(max_length=2, choices = GENDER_CHOICES, default=
            MALE, blank=True, null=True)
    telephone = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'


