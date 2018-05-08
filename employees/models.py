from django.db import models


class EmployeeDetails(models.Model):
    emp_name = models.CharField(default="Employee name", max_length=200)
    emp_title = models.CharField(default="Title",max_length=100)
    emp_bio = models.TextField(default="I love the agency")
    emp_image = models.ImageField(upload_to='Images/', default='Img.jpg')



