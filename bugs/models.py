from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bug(models.Model):
    """Choices"""
    ISSUE_TYPE = (
        ('Bug', 'Bug'),
        ('Feature', 'Feature')
    )
        
    TICKET_STATUS = (
        ('Todo', 'Todo'),
        ('Doing', 'Doing'),
        ('Done', 'Done')
    )
   
    title = models.CharField(max_length=100, blank=False)
    
    ticket_status = models.CharField(
        choices=TICKET_STATUS,
        default='Todo'
    )
    
    issue_type = models.CharField(
        choices=ISSUE_TYPE,
        default='Feature'
    )
    
    description = models.TextField(blank=False)
    
    views = models.BigIntegerField(
        default=0)
        
    upvotes = models.IntegerField(
        default=0 )
    
    
    def __str__(self):
        return self.name