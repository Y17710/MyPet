from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Post

# Board 페이지 기본
def index(request):
    return render(request, 'index_board.html')

# Board 기본 페이지 내 iframe에 DB에 저장된 포스트 출력
def posting(request):
    postlist = Post.objects.all()
    return render(request, 'posting.html', {'postlist':postlist})

# 새로운 포스트 작성
def newpost(request):
    return render(request, 'newpost.html')

# 작성한 새로운 포스트를 업로드
# 포스트 제목과 내용은 각각 Post 객체에 저장하여 DB에 저장
def uploadpost(request):    
    if request.method == 'POST':
        newpost = Post()
        newpost.postname = request.POST['postname']
        newpost.contents = request.POST['contents']
        newpost.save()
        return redirect('posting')
    elif request.method == 'GET':
        return redirect('posting')