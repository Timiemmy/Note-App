from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, db_index=True)
    username = models.CharField(max_length=20, unique=True, db_index=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.email
    

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', blank=True, null=True, default='profile_pics/default-profile-picture1.jpg')


    def __str__(self):
        return f'{self.username} profile'
    
    # Overriding the image 
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)