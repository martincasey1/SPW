from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import RegexValidator
from PIL import Image


alphanumeric = RegexValidator(r'^[A-Za-z\d\s]*$', 'Only alphanumeric characters are allowed.')
# Create your models here.
class Post(models.Model):
  
    title = models.CharField(max_length=100, validators=[alphanumeric])
    content = models.TextField(validators=[alphanumeric])
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_post')


    def total_likes(self):
        return self.likes.count()
 
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('post-detail', kwargs={'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(validators=[alphanumeric])
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_added']

    #def __str__(self):
        #return '%s %s' % (self.body)


class Gallery(models.Model):
    name = models.CharField(max_length=50, validators=[alphanumeric])
    gallery_Main_Img = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.gallery_Main_Img.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.gallery_Main_Img.path)


class Contact(models.Model):
    email_allowed = RegexValidator(r'^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$', 'Only alphanumeric, "@" and "." characters are allowed.')
    first_name = models.CharField(max_length = 50, validators=[alphanumeric])
    last_name = models.CharField(max_length = 50, validators=[alphanumeric])
    email_address = models.EmailField(max_length = 150, validators=[email_allowed])
    message = models.CharField(max_length = 2000, validators=[alphanumeric])