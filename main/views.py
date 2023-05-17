from django.shortcuts import render
from django.http import HttpResponse

# MyPet Main 페이지
def index(request):
    return render(request, 'index.html')