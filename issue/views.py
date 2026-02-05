from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Issue
from books.models import Books

@login_required
def issue_book(request, book_id):
    book = Books.objects.get(id=book_id)

    if book.quantity > 0:
        Issue.objects.create(
            student=request.user,
            book=book,
            issue_date=timezone.now()
        )
        book.quantity -= 1
        book.save()

        return render(request, "issue_success.html")

    return render(request, "no_stock.html")


@login_required
def return_book(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    issue.return_date = timezone.now().date()
    issue.save()

    book = issue.book
    book.quantity += 1
    book.save()

    return render(request, "return_success.html")


@login_required
def issue_history(request):
    history = Issue.objects.filter(student=request.user)
    return render(request, "issue_history.html", {"history": history})



