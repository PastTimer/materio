from django.views.generic import TemplateView
from web_project import TemplateLayout
from bookshelf.models import Book, Bookshelf, Author
from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import ExtractMonth
from datetime import datetime

class DashboardsView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['books_count'] = Book.objects.count()
        context['bookshelves_count'] = Bookshelf.objects.count()
        context['authors_count'] = Author.objects.count()
        context['books'] = Book.objects.order_by('-created_at')[:5]
        context['authors'] = Author.objects.order_by('-joined_date')[:5]
        return context
