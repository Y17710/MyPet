from django.contrib import admin
from .models import Post

# Post 관리할 수 있도록 DB에 등록
admin.site.register(Post)
