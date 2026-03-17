from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout, get_user_model

User = get_user_model()

def signup_view(request):

    if request.method == "POST": 

        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        User.objects.create_user(
            username=username,
            password=password,
            role=role
        )

        return redirect("login")

    return render(request,"signup.html")


def login_view(request):

    error = None

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("dashboard")
        else:
            error = "Invalid username or password"

    return render(request,"login.html",{"error":error})


def logout_view(request):

    logout(request)
    return redirect('login')