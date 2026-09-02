from django.shortcuts import render
from .models import Experience


def home(request):
    experiences = Experience.objects.all()

    return render(
        request,
        "core/home.html",
        {"experiences": experiences}
    )