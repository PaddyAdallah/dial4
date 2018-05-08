from django.shortcuts import render

from .models import EmployeeDetails


def index_view(request):
    details = EmployeeDetails.objects.all()

    context = {
        "details": details,
    }

    return render(request, "Employees/index.html", context)


def about_view(request):
    details = EmployeeDetails.objects.all()

    context = {
        "details": details,
    }

    return render(request, "Employees/about.html",context)


def gallery_view(request):
    details = EmployeeDetails.objects.all()

    context = {
        "details": details,
    }

    return render(request, "Employees/gallery.html", context)


def contact_view(request):
    details = EmployeeDetails.objects.all()

    context = {
        "details": details,
    }

    return render(request, "Employees/contact.html", context)


def employee_view(request):
    details = EmployeeDetails.objects.all()

    context = {
        "details": details,
    }

    return render(request, "Employees/profiles.html", context)
