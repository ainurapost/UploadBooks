from django.contrib.auth.decorators import permission_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
import random, datetime

from .models import Books, Comment
from .forms import CommentForm, AddBookForm


def index(request):
    books = Books.objects.all()
    paginator = Paginator(Books.objects.all(), 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'books': books,
        'title': 'Book list',
        'page_obj': page_obj,

    }
    return render(request, 'books/index.html', context)


def detail(request, book_id):
    book = get_object_or_404(Books, pk=book_id)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            com = form.save(commit=False)
            com.book = book
            com.save()
    comments = Books.objects.filter(book=book_id)
    context = {'book': book, 'form': form, 'comments': comments}
    return render(request, 'books/detail.html', context)


@permission_required('books.add')
def add(request):
    form = AddBookForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AddBookForm()

    return render(request, 'books/add.html', {'form': form, })


def new_list(request):
    newbooks = Books.objects.all().order_by('-created_at')[0:3]

    return render(request, 'books/new_list.html', {'books': newbooks})


def random_list(request):
    books = list(Books.objects.all())
    random_l = random.sample(books, 3)
    return render(request, 'books/random_list.html', {'random_l': random_l})
