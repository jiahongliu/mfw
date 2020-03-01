from django.db import models

# Create your models here.
#一个Django项目用一个MySQL 数据库

class Article(models.Model):
    title=models.CharField(max_length=32,default='Title')
    content=models.TextField(null=True)

    def __unicode__(self):
        return self.title

class Travel(models.Model):
    title=models.CharField(max_length=45)
    author=models.CharField(max_length=45)
    ding=models.CharField(max_length=45)
    content=models.CharField(max_length=225)
    img_url=models.URLField(max_length=225)
