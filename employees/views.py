from rest_framework import viewsets
from .models import EmployeeDetails
from .serializers import PostSerializer

from django.shortcuts import render_to_response


class PostViewSet(viewsets.ModelViewSet):
    queryset = EmployeeDetails.objects.all()
    serializer_class = PostSerializer


def index(request):
    return render_to_response('index.html')


def about(request):
    return render_to_response('about.html')


def gallery(request):
    return render_to_response('gallery.html')


def contact(request):
    return render_to_response('contact.html')
