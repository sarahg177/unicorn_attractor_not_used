from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bug(models.Model):
    """Choices"""
    issue_type = (
        ('Bug', 'Bug'),
        ('Feature', 'Feature')
    )
        
    ticket_status = (
        ('Todo', 'Todo'),
        ('Doing', 'Doing'),
        ('Done', 'Done')
    )
   
    title = models.CharField(max_length=100, blank=False)
    
    ticket_status = models.CharField(
        max_length=50,
        #choices=ticket_status,
        default='Todo'
    )
    
    issue_type = models.CharField(
        max_length=50,
      #  choices=issue_type,
        default='Feature'
    )
    
    description = models.TextField(blank=False)
    
    views = models.IntegerField(
        default=0)
        
    upvotes = models.IntegerField(
        default=0 )
    
    
    def __str__(self):
        return self.name