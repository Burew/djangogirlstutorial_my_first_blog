from django.db import models
from django.utils import timezone


"""
    TO make updates to the Models in database, add models here, then on the cmd line:
        python manage.py makemigrations APPNAME
        python manage.py migrate APPNAME

    in this case, APPNAME is : blog
"""

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()   
    created_date = models.DateTimeField(
        default = timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
 
