from django.shortcuts import render
from django.views.generic import ListView
from .models import Author, Book, Bookshelf
from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import ExtractMonth
from datetime import datetime
from web_project import TemplateLayout  # Add this import

class AuthorListView(ListView):
    model = Author
    template_name = 'bookshelf/author_list.html'
    context_object_name = 'authors'

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context

class BookListView(ListView):
    model = Book
    template_name = 'bookshelf/book_list.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context

class BookshelfListView(ListView):
    model = Bookshelf
    template_name = 'bookshelf/bookshelf_list.html'
    context_object_name = 'bookshelves'

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context

def books_per_bookshelf(request):
    data = (
        Bookshelf.objects
        .annotate(book_count=Count('books'))
        .values('name', 'book_count')
    )
    labels = [item['name'] for item in data]
    counts = [item['book_count'] for item in data]
    return JsonResponse({'labels': labels, 'data': counts})


def books_added_per_month(request):
    current_year = datetime.now().year
    month_map = {
        1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr',
        5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
        9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
    }

    data = (
        Book.objects.filter(created_at__year=current_year)
        .annotate(month=ExtractMonth('created_at'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )

    month_counts = {month: 0 for month in month_map.values()}
    for entry in data:
        month_name = month_map.get(entry['month'])
        if month_name:
            month_counts[month_name] = entry['count']

    return JsonResponse({
        'labels': list(month_counts.keys()),
        'data': list(month_counts.values())
    })
