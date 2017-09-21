from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    alt_text = models.CharField(max_length=80, blank=True, null= True)
    thumbnail_path = models.CharField(max_length=100,blank=True, null=True, default=None)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Caption(models.Model):
    post = models.ForeignKey('blog.Post', related_name='caption')
    caption = models.CharField(max_length=300)
    order = models.IntegerField(blank=True, null=True, default=None)
    color = models.CharField(max_length = 15, default='255,255,255')
    backcolor = models.CharField(max_length = 15, default='0,0,0')

    def __str__(self):
        return self.caption