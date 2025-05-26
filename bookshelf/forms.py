from django import forms
from django.forms import ModelForm
from .models import Bookshelf, Book, Author

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'middle_name': forms.TextInput(attrs={'placeholder': 'Middle Name (optional)'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }
        labels = {
            'first_name': 'First Name',
            'middle_name': 'Middle Name',
            'last_name': 'Last Name',
        }

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Book Title'}),
            'author': forms.Select(),
        }
        labels = {
            'title': 'Book Title',
            'author': 'Author',
        }

class BookshelfForm(ModelForm):
    class Meta:
        model = Bookshelf
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Bookshelf Name'}),
            'books': forms.SelectMultiple(),
        }
        labels = {
            'name': 'Bookshelf Name',
            'books': 'Books in this Shelf',
        }
