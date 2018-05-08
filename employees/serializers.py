from .models import EmployeeDetails
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):

    emp_image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = EmployeeDetails
        fields = ("emp_name", "emp_title", "emp_bio", "emp_image")
