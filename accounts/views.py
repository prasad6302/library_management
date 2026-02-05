from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Student


def register_student(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        roll_no = request.POST.get("roll_no")
        department = request.POST.get("department")

        # Check duplicate username
        if User.objects.filter(username=username).exists():
            return render(request, "student_register.html", {"error": "Username already exists","register_page": True})

        # Create user
        user = User.objects.create_user(username=username, password=password)

        # Create Student Profile
        Student.objects.create(
            user=user,
            roll_no=roll_no,
            department=department
        )

        return redirect("login")

    return render(request, "student_register.html",{"register_page": True})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("login")
