from .models import Book

from django.views import generic


class IndexView(generic.ListView):
    template_name = 'library1/index.html'
    context_object_name = 'latest_book_list'

    def get_queryset(self):
        return Book.objects.all()
