from django.db import models
from django.utils import timezone

class HomePost(models.Model):
    author = models.ForeignKey('auth.User')
    profile = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    birth_from = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phno = models.CharField(max_length=200)
    planguage = models.CharField(max_length=200)
    career = models.CharField(max_length=200)
    wexperience = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.profile