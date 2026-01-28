from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        return self.title


class Loan(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='loans'
    )
    borrower = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    loan_date = models.DateField(auto_now_add=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book.title} - {self.borrower.username}"
