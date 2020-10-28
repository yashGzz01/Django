from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    