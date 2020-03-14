from django.shortcuts import render, redirect
from .models import Helper
from ukpostcodeutils import validation


def home_page(request):
    return render(request, "home.html")


def add_helper(request):
    postcode = request.POST["postcodeFirst"] + request.POST["postcodeSecond"]
    if validation.is_valid_postcode(postcode):
        Helper.objects.create(
            postcodeFirst=request.POST["postcodeFirst"],
            postcodeSecond=request.POST["postcodeSecond"],
            link=request.POST["link"],
        )
        return render(request, "thankyou.html")
    else:
        return render(request, "error.html", {"postcode": postcode})


def need_help(request):
    return render(request, "needhelp.html")


def postcode_search(request):
    pass
