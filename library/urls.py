from django.urls import path
from .views import (
    author_list, author_detail,
    book_list, book_detail,
    loan_list, loan_detail
)

urlpatterns = [
    path('authors/', author_list),
    path('authors/<int:pk>/', author_detail),

    path('books/', book_list),
    path('books/<int:pk>/', book_detail),

    path('loans/', loan_list),
    path('loans/<int:pk>/', loan_detail),
]
