from django.core.management.base import BaseCommand
from users.models import User
from expenses.models import Category, Expense
from decimal import Decimal
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Populate the database with sample data for testing'

    def handle(self, *args, **options):
        # Create sample users
        user1, created = User.objects.get_or_create(
            username='john_doe',
            defaults={
                'email': 'john@example.com',
                'first_name': 'John',
                'last_name': 'Doe'
            }
        )
        if created:
            user1.set_password('password123')
            user1.save()
            self.stdout.write(self.style.SUCCESS(f'Created user: {user1.username}'))
        
        user2, created = User.objects.get_or_create(
            username='jane_smith',
            defaults={
                'email': 'jane@example.com',
                'first_name': 'Jane',
                'last_name': 'Smith'
            }
        )
        if created:
            user2.set_password('password123')
            user2.save()
            self.stdout.write(self.style.SUCCESS(f'Created user: {user2.username}'))
        
        # Create sample categories
        categories_data = [
            {'name': 'Food'},
            {'name': 'Travel'},
            {'name': 'Entertainment'},
            {'name': 'Shopping'},
            {'name': 'Utilities'}
        ]
        
        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(**cat_data)
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))
        
        # Create sample expenses
        expenses_data = [
            {'title': 'Lunch at restaurant', 'amount': Decimal('25.50'), 'category': categories['Food'], 'user': user1, 'date': date.today()},
            {'title': 'Movie tickets', 'amount': Decimal('15.00'), 'category': categories['Entertainment'], 'user': user1, 'date': date.today()},
            {'title': 'Bus fare', 'amount': Decimal('5.00'), 'category': categories['Travel'], 'user': user1, 'date': date.today()},
            {'title': 'Groceries', 'amount': Decimal('120.75'), 'category': categories['Food'], 'user': user2, 'date': date.today()},
            {'title': 'Flight tickets', 'amount': Decimal('500.00'), 'category': categories['Travel'], 'user': user2, 'date': date.today()},
            {'title': 'Concert tickets', 'amount': Decimal('80.00'), 'category': categories['Entertainment'], 'user': user2, 'date': date.today()},
            {'title': 'Electricity bill', 'amount': Decimal('85.50'), 'category': categories['Utilities'], 'user': user1, 'date': date.today() - timedelta(days=1)},
            {'title': 'Coffee', 'amount': Decimal('4.50'), 'category': categories['Food'], 'user': user1, 'date': date.today() - timedelta(days=1)},
            {'title': 'Shopping mall', 'amount': Decimal('150.00'), 'category': categories['Shopping'], 'user': user2, 'date': date.today() - timedelta(days=2)},
            {'title': 'Gas station', 'amount': Decimal('45.00'), 'category': categories['Travel'], 'user': user1, 'date': date.today() - timedelta(days=2)},
        ]
        
        for expense_data in expenses_data:
            expense, created = Expense.objects.get_or_create(**expense_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created expense: {expense.title} - ${expense.amount}'))
        
        self.stdout.write(self.style.SUCCESS('\nSample data created successfully!'))
        self.stdout.write(f'Total users: {User.objects.count()}')
        self.stdout.write(f'Total categories: {Category.objects.count()}')
        self.stdout.write(f'Total expenses: {Expense.objects.count()}')
