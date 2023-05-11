from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField 
class User(AbstractUser):
    phone = models.CharField(max_length=20)
    avatar=models.ImageField(null=True,default="avatar.png",blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f' Name :{self.username} '
class Blog(models.Model):
    post = RichTextField()
    post_image = models.ImageField(null=True, blank=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.post    
    
class Comment(models.Model):
    comment_by=models.ForeignKey(User,on_delete=models.CASCADE)
    blog_commented=models.ForeignKey( Blog,on_delete=models.CASCADE)
    comment_body=models.TextField()
    reply = models.ForeignKey('self', null=True, blank=True, related_name='replies',on_delete=models.CASCADE)
    create_timestamp=models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.comment_body    


