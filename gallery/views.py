from django.shortcuts import render
from django.http import HttpResponse

# Gallery 페이지 기본
def index(request):
    return render(request, 'index_gallery.html')