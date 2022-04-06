from csv import DictReader
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_obj = Book.objects.all()
    context = {
        'books': books_obj,
    }
    return render(request, template, context)


def book_pagi(request, date):
    template = 'books/book.html'
    book_obj = Book.objects.filter(pub_date=date)
    all_books = Book.objects.all()
    paginator = Paginator(all_books, 2)
    page_number = request.GET.get('page', 2)
    page_obj = paginator.get_page(page_number)
    for i in book_obj:
       book_name = i.name 
       book_author = i.author
       book_pub_date = i.pub_date
    context = {
        'book_name': book_name,
        'book_author': book_author,
        'book_pub_date':book_pub_date,
        'pagi': page_obj,
    }
        
    return render(request, template, context)


