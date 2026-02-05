
from django.urls import path
from .views import dashboard, books_list, add_book

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("list/", books_list, name="books_list"),
    path("add/", add_book, name="add_book"),
]
