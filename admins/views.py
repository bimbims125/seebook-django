from ast import Add
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import AddBookForms
from core.models import Books
# Create your views here.

class DashboardView(View):
    def get(self, request):
        return render(request, 'home.html')

class BooksView(View):

    def get(self, request):        
        book = Books.objects.all()
        form = AddBookForms()
        context = {
            'book':book,
            'form':form            
        }
        return render(request, 'admin-menu/books.html', context)    

    def post(self, request):
        form = AddBookForms(request.POST or None, request.FILES or None)
        if form.is_valid():                      
            form.save()
            return redirect('books')


class DeleteBookView(View):
    def get(self, request, pk):
        book = Books.objects.get(id=pk)
        context = {
            'book':book
        }
        return render(request, 'admin-menu/delete.html', context)

    def post(self, request, pk):
        book = Books.objects.get(id=pk)
        book.delete()
        return redirect('books')        