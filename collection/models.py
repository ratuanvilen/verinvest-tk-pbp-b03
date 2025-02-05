from django.db import models
from profile_page.models import Profile

class Post(models.Model):
    post_type = models.CharField(max_length=10)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    date_created = models.DateField(auto_now_add=True)
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    upvotes = models.IntegerField()
    viewers = models.IntegerField()
    comments_count = models.IntegerField()