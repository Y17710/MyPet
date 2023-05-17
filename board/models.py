from django.db import models

# 게시판 포스트 제목과 내용을 저장하는 Post 객체
# 포스트 제목으로 객체 식별
class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()
    
    def __str__(self):
        return self.postname

# Create your models here.
