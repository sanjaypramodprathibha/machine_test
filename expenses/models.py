from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    """
    Category model for expense categorization
    """
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        db_table = 'expenses_category'
    
    def __str__(self):
        return self.name


class Expense(models.Model):
    """
    Expense model with category relationship
    """
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='expenses')
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    
    class Meta:
        db_table = 'expenses_expense'
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.title} - {self.amount}"