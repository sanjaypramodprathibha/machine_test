# Interview Demo Script - Django REST API

## 🎯 **5-Minute Live Demo Plan**

### **Step 1: Quick Setup (30 seconds)**
```bash
cd /path/to/project
source venv/bin/activate
python manage.py runserver
```

### **Step 2: Show Empty State (30 seconds)**
```bash
# Show initial empty state
curl http://127.0.0.1:8000/users/
curl http://127.0.0.1:8000/categories/
curl http://127.0.0.1:8000/expenses/
curl http://127.0.0.1:8000/expenses/summary/
```

### **Step 3: Live Data Creation (3 minutes)**

#### **Create Categories:**
```bash
curl -X POST http://127.0.0.1:8000/categories/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Food"}'

curl -X POST http://127.0.0.1:8000/categories/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Travel"}'

curl -X POST http://127.0.0.1:8000/categories/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Entertainment"}'
```

#### **Register Users:**
```bash
curl -X POST http://127.0.0.1:8000/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "john_doe", "email": "john@example.com", "password": "password123", "password_confirm": "password123"}'

curl -X POST http://127.0.0.1:8000/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "jane_smith", "email": "jane@example.com", "password": "password123", "password_confirm": "password123"}'
```

#### **Create Expenses:**
```bash
curl -X POST http://127.0.0.1:8000/expenses/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Lunch at restaurant", "amount": "25.50", "category": 1, "date": "2025-10-09"}'

curl -X POST http://127.0.0.1:8000/expenses/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Bus fare", "amount": "5.00", "category": 2, "date": "2025-10-09"}'

curl -X POST http://127.0.0.1:8000/expenses/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Movie tickets", "amount": "15.00", "category": 3, "date": "2025-10-09"}'

curl -X POST http://127.0.0.1:8000/expenses/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Flight tickets", "amount": "500.00", "category": 2, "date": "2025-10-09"}'
```

### **Step 4: Show Results (1 minute)**
```bash
# Show all users
curl http://127.0.0.1:8000/users/

# Show all categories
curl http://127.0.0.1:8000/categories/

# Show all expenses
curl http://127.0.0.1:8000/expenses/

# Show the magic - expense summary with Django ORM aggregation
curl http://127.0.0.1:8000/expenses/summary/
```

### **Step 5: Show Validation (30 seconds)**
```bash
# Show validation errors
curl -X POST http://127.0.0.1:8000/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "ab", "email": "invalid", "password": "short", "password_confirm": "different"}'
```

---

## 🚀 **Quick Demo Commands (Copy-Paste Ready)**

### **One-Liner Setup:**
```bash
cd /path/to/project && source venv/bin/activate && python manage.py runserver &
```

### **Create Sample Data (Run in another terminal):**
```bash
# Categories
curl -X POST http://127.0.0.1:8000/categories/ -H "Content-Type: application/json" -d '{"name": "Food"}' && \
curl -X POST http://127.0.0.1:8000/categories/ -H "Content-Type: application/json" -d '{"name": "Travel"}' && \
curl -X POST http://127.0.0.1:8000/categories/ -H "Content-Type: application/json" -d '{"name": "Entertainment"}'

# Users
curl -X POST http://127.0.0.1:8000/register/ -H "Content-Type: application/json" -d '{"username": "john_doe", "email": "john@example.com", "password": "password123", "password_confirm": "password123"}' && \
curl -X POST http://127.0.0.1:8000/register/ -H "Content-Type: application/json" -d '{"username": "jane_smith", "email": "jane@example.com", "password": "password123", "password_confirm": "password123"}'

# Expenses
curl -X POST http://127.0.0.1:8000/expenses/ -H "Content-Type: application/json" -d '{"title": "Lunch", "amount": "25.50", "category": 1, "date": "2025-10-09"}' && \
curl -X POST http://127.0.0.1:8000/expenses/ -H "Content-Type: application/json" -d '{"title": "Bus", "amount": "5.00", "category": 2, "date": "2025-10-09"}' && \
curl -X POST http://127.0.0.1:8000/expenses/ -H "Content-Type: application/json" -d '{"title": "Movie", "amount": "15.00", "category": 3, "date": "2025-10-09"}' && \
curl -X POST http://127.0.0.1:8000/expenses/ -H "Content-Type: application/json" -d '{"title": "Flight", "amount": "500.00", "category": 2, "date": "2025-10-09"}'
```

### **Show Results:**
```bash
curl http://127.0.0.1:8000/expenses/summary/ | python3 -m json.tool
```

---

## 💡 **Key Points to Highlight During Demo**

1. **"I'll start with an empty database and create data live"**
2. **"Notice the validation working - username must be 5+ chars, email must be valid, password must be 8+ chars with a number"**
3. **"Here's the Django ORM aggregation in action - expense summary grouped by category"**
4. **"All relationships work - expenses are linked to categories and users"**
5. **"Proper HTTP status codes - 201 for creation, 400 for validation errors"**

---

## 🎯 **Demo Script for Interviewers**

**"Let me show you this Django REST API I built. I'll start with a fresh database and create data live to demonstrate all the features."**

1. **Start server** (30 seconds)
2. **Show empty endpoints** (30 seconds)
3. **Create categories** (30 seconds)
4. **Register users with validation** (1 minute)
5. **Create expenses** (1 minute)
6. **Show expense summary with Django ORM aggregation** (30 seconds)
7. **Show validation errors** (30 seconds)

**Total: 5 minutes of live demonstration!**
