# from django.shortcuts import render
# from .models import Books
# import datetime
# # Create your views here.

# def dashboard(request):
#     books = Books.objects.all()
#     date = datetime.datetime.now()

#     return render(request,'dashboard.html',{'books':books,'date':date})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Books

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def books_list(request):
    books = Books.objects.all()
    return render(request, "books_list.html", {"books": books})

@login_required
def add_book(request):
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        category = request.POST["category"]
        quantity = int(request.POST["quantity"])

        Books.objects.create(
            title=title,
            author=author,
            category=category,
            quantity=quantity
        )
        return redirect("books_list")

    return render(request, "add_book.html")
