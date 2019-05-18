from django.db import models

# Create your models here.
class question(models.Model):
    subject = models.CharField(max_length=10) # 科目
    topic = models.CharField(max_length=500) # 題幹
    optionA = models.CharField(max_length=500) # 選項A
    optionB = models.CharField(max_length=500) # 選項B
    optionC = models.CharField(max_length=500) # 選項C
    optionD = models.CharField(max_length=500) # 選項D
    Answer = models.CharField(max_length=500) # 答案
    hint = models.CharField(max_length=500) # 提示
    remove = models.CharField(max_length=10) # 刪去選項

    def __str__(self):
        return self.topic

class player(models.Model):
    name = models.CharField(max_length=50) # 名字
    no_Q = models.IntegerField(default=0) # 答對題數
    score = models.IntegerField(default=0) # 分數
    no_remove = models.IntegerField(default=0) # 刪去題數
    no_hint = models.IntegerField(default=0) # 提示題數

    def __str__(self):
        return self.name