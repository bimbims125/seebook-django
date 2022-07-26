from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def allBooks(request):
    return render(request, 'all_books.html')