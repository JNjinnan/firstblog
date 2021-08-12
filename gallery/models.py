from django.db import models
# model用来实现组件的功能
# Create your models here.
# 当创建了新的model就要做迁移文件

class Gallery(models.Model):
    description=models.CharField(max_length=100)  # 创建结束后，要在admin中进行注册
