from django.shortcuts import render, redirect
from .models import Helper


def home_page(request):
    return render(request, "home.html")


def add_helper(request):
    Helper.objects.create(
        postcode=request.POST["postcode"], link=request.POST("link")
    )
    return redirect("thankyou.html")
