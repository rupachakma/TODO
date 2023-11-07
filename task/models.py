from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasklist(models.Model):

    status_choices = [
    ("C", "COMPLETEd"),
    ("P", "PENDING"),   
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=2,choices=status_choices)
    createat = models.DateTimeField(auto_now_add=True)
    schedule = models.TimeField()

def __str__(self):
    return self.title

class Profileimg(models.Model):
    profilepic = models.ImageField(upload_to="img",blank=True,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
def __str__(self):
    return str(self.user)