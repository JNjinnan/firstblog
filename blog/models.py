from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(default='新闻标题',max_length=50)
    date=models.DateField()
    image=models.ImageField(default='default.png',upload_to='images/')
    text=models.CharField(default='新闻正文',max_length=500)

    def __str__(self):
        return self.title