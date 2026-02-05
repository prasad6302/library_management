from django.urls import path
from .views import issue_book, return_book, issue_history

urlpatterns = [
    path("issue/<int:book_id>/", issue_book, name="issue_book"),
    path("return/<int:issue_id>/", return_book, name="return_book"),
    path("history/", issue_history, name="issue_history"),
]
