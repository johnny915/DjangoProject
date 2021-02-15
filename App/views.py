from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from .forms import register_form
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import product, cart, profile
from django.contrib.auth.models import User


def index(request):
    item = product.objects.all()
    return render(request, "content.html", {"item": item})


@login_required(login_url='logedin')
def cart_item(request):
    id = request.POST.get("id")
    item = get_object_or_404(product, product_id=id)
    length = len(cart.objects.filter(product_cart=id))
    if (length > 0):
        print("this is already exist")
    else:
        c = cart(product_cart=item)
        c.save()

    Cart = cart.objects.all()

    return render(request, "cart.html", {"Cart": Cart})


@login_required(login_url='logedin')
def display_cart(request):
    Cart = cart.objects.all()

    return render(request, "cart.html", {"Cart": Cart})


def logedin(request):
    if request.method == "POST":
        username = request.POST.get("username");
        password = request.POST.get("password");

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")

    return render(request, "login.html")


def signup(request):
    form = register_form()
    if request.method == "POST":
        form = register_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("logedin")

    return render(request, "sign_up.html", {"form": form})


def log_out(request):
    logout(request)
    return render(request, "login.html")


def search(request):
    if request.method == "POST":
        qry = request.POST.get("qry")
        product_res = product.objects.filter(product_name__contains=qry)
        print("result is === ", product_res)
    else:
        print("invalid query")
    return render(request, "result.html", {"result": product_res})


@login_required(login_url='logedin')
def checkout(request):
    cart_1 = cart.objects.all()
    return render(request, "checkout.html", {"context": cart_1})


def user(request):
    if (request.method == "POST"):
        phon1 = request.POST.get("phon1")
        phon2 = request.POST.get("phon2")
        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zipcode = request.POST.get("zipcode")

    user_info = User.objects.get(username=request.user.username)

    Profile = profile(user_detail=user_info, phon1=phon1,
                      phon2=phon2, address1=address1, address2=address2,
                      city=city, state=state, zipcode=zipcode)
    Profile.save()
    cart_1 = cart.objects.all()
    var = ""
    for i in cart_1:
        var += i.product_cart.product_name + " Price is " + i.product_cart.product_price + "\n"
    send_mail(
        "Order Details",
        "Thank you for shopping with us \n" + "Your order is placed successfully , You ordered : \n " + var,
        settings.EMAIL_HOST,
        [user_info.email],
        fail_silently=False,
    )

    return redirect("feedback")
    return render(request, "checkout.html", {"context": cart_1})


def feedback(request):
    user_info = User.objects.get(username=request.user.username)
    return render(request,"feedback.html",{"context":user_info})