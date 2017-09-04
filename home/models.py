from django.db import models
from django.utils import timezone

class HomePost(models.Model):
    
    def __str__(self):
        return self.HomePost