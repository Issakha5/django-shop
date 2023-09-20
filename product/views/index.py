from django.contrib.auth import login
from django.shortcuts import render, redirect
from ..models.product import Product
from ..forms import SignUpForm


def home(request):
    products = Product.objects.all()[0:8]

    return render(request, "product/index.html", context={"products": products})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("/")
    else:
        form = SignUpForm()

    return render(request, "product/signup.html", {"form": form})


def account(request):
    return render(request, "product/account.html")


def edit_account(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        user.username = request.POST.get("username")
        user.save()

        return redirect("account")
    return render(request, "product/edit_account.html")
