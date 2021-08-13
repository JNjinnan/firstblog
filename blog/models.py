from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(default='新闻标题',max_length=50)
    date=models.DateField()
    image=models.ImageField(default='default.png',upload_to='images/')
    text=models.TextField(default='新闻正文')

    def __str__(self):
        return self.title

    def short_text(self):
        return self.text[:60]+'...'  #字符串切片，只显示文章前100个字