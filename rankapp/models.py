from django.db import models

# Create your models here.
class PostModel(models.Model):
    post_type = models.CharField(max_length=100)
    post_url = models.CharField(max_length=200)
    note_count = models.IntegerField()
    # text用
    title = models.TextField(null=True, default='')
    body = models.TextField(null=True, default='')
    # photo用
    caption = models.TextField(null=True, default='')
    link = models.TextField(null=True, default='')
    images = models.ImageField(upload_to='', null=True, default='static/default.png')
