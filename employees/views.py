from rest_framework import viewsets
from .models import EmployeeDetails
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = EmployeeDetails.objects.all()
    serializer_class = PostSerializer


