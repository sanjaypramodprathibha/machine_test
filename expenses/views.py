from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer


class CategoryListView(generics.ListCreateAPIView):
    """
    GET /categories/ - List all categories
    POST /categories/ - Create new category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ExpenseListView(generics.ListCreateAPIView):
    """
    GET /expenses/ - List all expenses
    POST /expenses/ - Create new expense
    """
    queryset = Expense.objects.select_related('category', 'user').all()
    serializer_class = ExpenseSerializer


@api_view(['GET'])
def expense_summary(request):
    """
    GET /expenses/summary/ - Get total expense amount grouped by category
    """
    # Use Django ORM aggregation to calculate totals by category
    summary_data = Expense.objects.values('category__name').annotate(
        total_amount=Sum('amount')
    ).order_by('category__name')
    
    # Convert to the required format
    result = {}
    for item in summary_data:
        result[item['category__name']] = float(item['total_amount'])
    
    return Response(result, status=status.HTTP_200_OK)