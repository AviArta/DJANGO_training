from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import F, Min, Max

from books.models import Book


def hello(request):
    text_hello = 'Добро пожаловать в книжный магазин!'
    return render(request, 'books/hello.html', {'text': text_hello})


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    # pub_dates = []
    # for book in books:
    #     pub_dates.append(book.pub_date)
    return render(request, template, {'books': books})


def book_page(request, book_id):
    template = 'books/book_info.html'
    book = get_object_or_404(Book, id=book_id)
    context = {'book': book,
               'book_id': book.id,
               'pub_date': book.pub_date}
    return render(request, template, context)


def by_date(request, pub_date):
    template = 'books/by_date_1.html'
    # books = Book.objects.filter(pub_date=pub_date)
    books_obj = get_list_or_404(Book, pub_date=pub_date)
    try:
        previous = books_obj[-1].get_previous_by_pub_date()
    except:
        previous = None
    try:
        next = books_obj[-1].get_next_by_pub_date()
    except:
        next = None
    context = {'books_obj': books_obj,
               'pub_date': pub_date,
               'previous': previous,
               'next': next
               }
    return render(request, template, context)

    # < a
    # href = "{% url 'books' prev_date.pub_date|date:'Y-m-d' %}" > < button > {{prev_date}} < / button > < / a >

    # < a
    # href = "{% url 'books' next_date.pub_date|date:'Y-m-d' %}" > < button > {{next_date}} < / button > < / a >

    # на всякий случай, что смогла найти:
    # first_pub_date = Book.objects.aggregate(first_pub_date=Min('pub_date'))['first_pub_date']
    # last_pub_date = Book.objects.aggregate(last_pub_date=Max('pub_date'))['last_pub_date']

    # попытка:
    # books_sort = sorted(Book.objects.all(), key=lambda book: book.pub_date)
    # books_sort = [<Book: 1984 Джордж Оруэл>, <Book: Война и мир Ф.Д. Достоевский>, <Book: Скотный двор Джордж Оруэл>, <Book: В память о прошлом земли Лю Цысинь>]