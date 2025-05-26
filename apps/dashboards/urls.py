from django.urls import path
from .views import DashboardsView
from bookshelf.views import books_per_bookshelf, books_added_per_month

urlpatterns = [
    path("", DashboardsView.as_view(template_name="dashboard_analytics.html"), name="index"),
    path("charts/bookshelf-bar/", books_per_bookshelf, name="bookshelf_bar_chart"),
    path("charts/bookshelf-line/", books_added_per_month, name="bookshelf_line_chart"),
]
