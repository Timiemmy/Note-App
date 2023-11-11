from django.db import models
from django.utils import timezone
from django.urls import reverse
from accounts.models import CustomUser


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='',upload_to='images',blank=True,null=True)
    audio = models.FileField(default='',upload_to='audio',blank=True,null=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
