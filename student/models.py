from django.db import models
from django.utils.safestring import mark_safe

class Country(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name

class City(models.Model):
    Name = models.CharField(max_length=30, default='Mumbai')
    thumbnail = models.ImageField(null=True, upload_to='images/')
    
    def  image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.thumbnail))

    image_tag.allow_tags = True     
    
class Company(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

