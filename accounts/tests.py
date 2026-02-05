from django.test import TestCase

# Create your tests here.


# {% extends "base.html" %}
# <!-- <h2>Books</h2>
# {% for book in books %}
# <p>{{book.title | upper }} - {{book.author }} -->
# <!-- <p>{{book.title | length }} - {{book.author }} -->
# <!-- <p>{{book.title | join:', ' }} - {{book.author }} -->
# <!-- <p>{{book.title | truncatechars:10 }} - {{book.author }} -->
# <!-- <a href="{% url 'issue_book' book.id %}">Issue</a>
# </p>
# {% endfor %} -->
# <!-- <p>{{ date | date:'F D, Y' }}</p> -->
# <!-- <p>{{ date | date:'d-m-Y' }}</p> -->
# <!-- <p>{{ date | date:'H:i' }}</p> -->


# {% block content %}
# <h2 class="mb-3">Dashboard</h2>

# <div class="row">
#     <div class="col-md-6">
#         <h4>Available Books</h4>
#         <a href="{% url 'books_list' %}" class="btn btn-primary btn-sm mb-3">View Books</a>
#         <a href="{% url 'add_book' %}" class="btn btn-success btn-sm mb-3">Add Book</a>
#     </div>
   
#     <div class="col-md-6">
#         <h4>Issue / Return</h4>
#         <a href="/issue/history/" class="btn btn-warning btn-sm">Issue History</a>
#     </div>
# </div>

# {% endblock %}