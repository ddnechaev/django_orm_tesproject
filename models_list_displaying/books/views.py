from django.shortcuts import render
from books.models import Book

CONTENT = Book.objects.only()
def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, template, context)

def books_by_date_view(request, date):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)