from django.db import models

# Create your models here.
class Bug(models.Model):
    """Choices"""
    
   
    name = models.CharField(max_length=30, blank=False)
    
    description = models.TextField(blank=False)
    
    
    def __str__(self):
        return self.name