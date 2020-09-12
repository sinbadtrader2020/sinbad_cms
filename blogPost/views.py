
from django.shortcuts import render

# views.py
from rest_framework import viewsets

from .serializers import BLogSerializer
from .models import Blog
from rest_framework import permissions
from rest_framework.authtoken.models import Token

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('id')
    serializer_class = BLogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
import requests
# Create your views here.
def home(request):



    response = requests.get('http://127.0.0.1:8000/api/blogs')
    blogData=response.json()
    # return render(request,"index.html",{'dests':dests,'offer_count':offer_count})
    return  render(request,'home.html',{'dests':blogData})




#
# def home(request):
#     return render(request, 'home.html', {'name': 'Kiran'})