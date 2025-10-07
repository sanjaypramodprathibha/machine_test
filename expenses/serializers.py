from rest_framework import serializers
from .models import Category, Expense


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model
    """
    class Meta:
        model = Category
        fields = ('id', 'name')


class ExpenseSerializer(serializers.ModelSerializer):
    """
    Serializer for Expense model
    """
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Expense
        fields = ('id', 'title', 'amount', 'category', 'category_name', 'date', 'user')
        read_only_fields = ('user',)
    
    def create(self, validated_data):
        # Set user to a default user (user with ID 1) for testing purposes
        from users.models import User
        validated_data['user'] = User.objects.first()
        return super().create(validated_data)


class ExpenseSummarySerializer(serializers.Serializer):
    """
    Serializer for expense summary response
    """
    category_name = serializers.CharField()
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
