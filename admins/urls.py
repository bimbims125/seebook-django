from django.urls import path, include
from admins.views import *

urlpatterns = [
    path('admins/', include([
        path('dashboard', DashboardView.as_view(), name='dashboard'),
        path('books', BooksView.as_view(), name='books'),
        path('books/delete/<str:pk>', DeleteBookView.as_view(), name='delete')        
    ])),
    
]
