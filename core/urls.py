from django.urls import path, include
from .views import home, allBooks
urlpatterns = [
    path('', home, name='home'),
    path('book/', include([
        path('all-books', allBooks, name='all_books')
    ]))
]