#!/bin/bash

# Demo Data Creation Script
echo "🚀 Creating demo data for Django REST API..."

# Wait for server to be ready
sleep 2

echo "📝 Creating categories..."
curl -X POST http://127.0.0.1:8000/categories/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Food"}' > /dev/null

curl -X POST http://127.0.0.1:8000/categories/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Travel"}' > /dev/null

curl -X POST http://127.0.0.1:8000/categories/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Entertainment"}' > /dev/null

curl -X POST http://127.0.0.1:8000/categories/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Shopping"}' > /dev/null

echo "👥 Creating users..."
curl -X POST http://127.0.0.1:8000/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "john_doe", "email": "john@example.com", "password": "password123", "password_confirm": "password123"}' > /dev/null

curl -X POST http://127.0.0.1:8000/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "jane_smith", "email": "jane@example.com", "password": "password123", "password_confirm": "password123"}' > /dev/null

echo "💰 Creating expenses..."
curl -X POST http://127.0.0.1:8000/expenses/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Lunch at restaurant", "amount": "25.50", "category": 1, "date": "2025-10-09"}' > /dev/null

curl -X POST http://127.0.0.1:8000/expenses/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Bus fare", "amount": "5.00", "category": 2, "date": "2025-10-09"}' > /dev/null

curl -X POST http://127.0.0.1:8000/expenses/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Movie tickets", "amount": "15.00", "category": 3, "date": "2025-10-09"}' > /dev/null

curl -X POST http://127.0.0.1:8000/expenses/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Flight tickets", "amount": "500.00", "category": 2, "date": "2025-10-09"}' > /dev/null

curl -X POST http://127.0.0.1:8000/expenses/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Groceries", "amount": "120.75", "category": 1, "date": "2025-10-09"}' > /dev/null

curl -X POST http://127.0.0.1:8000/expenses/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Shopping mall", "amount": "150.00", "category": 4, "date": "2025-10-09"}' > /dev/null

echo "✅ Demo data created successfully!"
echo "🎯 Now show the results:"
echo "curl http://127.0.0.1:8000/expenses/summary/ | python3 -m json.tool"
