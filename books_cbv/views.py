from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from books_cbv.models import Book
# views.py
import logging
logger = logging.getLogger(__name__)


class BookList(ListView):
    model = Book

    def get_context_data(self, **kwargs):
        logger.debug("this is a debug message! ......................")
        cont = super(BookList,self).get_context_data(**kwargs)
        cont["data"] = "amira"
        return cont

class BookCreate(CreateView):
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('books_cbv:book_list')

class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('books_cbv:book_list')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books_cbv:book_list')


def myfunction():
    logger.debug("this is a debug message!")

def myotherfunction():
    logger.error("this is an error message!!")