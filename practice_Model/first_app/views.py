from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    author = models.Author.objects.all()
    return render(request,"home.html", {'authors': author})