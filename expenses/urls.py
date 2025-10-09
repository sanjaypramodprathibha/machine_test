from django.urls import path

from . import views


urlpatterns = [

path('categories/', views.CategoryListView.as_view(), name='category-list'),

path('expenses/', views.ExpenseListView.as_view(), name='expense-list'),

path('expenses/summary/', views.expense_summary, name='expense-summary'),

]

