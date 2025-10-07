# Django REST API Machine Test

This project implements a Django REST API with user management and expense tracking functionality.

## Features

1. **User Registration with Validation**
   - Username validation (minimum 5 characters)
   - Email validation (proper format)
   - Password validation (minimum 8 characters, must contain a number)

2. **User Management API**
   - Get all users
   - Get user by ID
   - Delete user by ID

3. **Expense Tracking**
   - Category management
   - Expense creation with category relationships
   - Expense summary grouped by category using Django ORM aggregation

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd machine-test-project
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Populate sample data (optional)**
   ```bash
   python manage.py populate_sample_data
   ```

## How to Run the Server

1. **Start the development server**
   ```bash
   source venv/bin/activate  # Activate virtual environment
   python manage.py runserver
   ```

2. **The server will start at**
   ```
   http://127.0.0.1:8000/
   ```

3. **Access Django Admin (if superuser created)**
   ```
   http://127.0.0.1:8000/admin/
   ```

## API Endpoints

### User Registration

**POST** `/register/`

Register a new user with validation.

**Request Body:**
```json
{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "password123",
    "password_confirm": "password123"
}
```

**Success Response (201):**
```json
{
    "message": "User registered successfully",
    "user": {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com",
        "date_joined": "2024-01-15T10:30:00Z"
    }
}
```

**Error Response (400):**
```json
{
    "message": "Registration failed",
    "errors": {
        "username": ["Username must be at least 5 characters long."],
        "password": ["Password must contain at least one number."]
    }
}
```

### User Management

**GET** `/users/`

Get all users.

**Response (200):**
```json
[
    {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com",
        "date_joined": "2024-01-15T10:30:00Z"
    },
    {
        "id": 2,
        "username": "jane_smith",
        "email": "jane@example.com",
        "date_joined": "2024-01-15T11:00:00Z"
    }
]
```

**GET** `/users/{id}/`

Get user by ID.

**Response (200):**
```json
{
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "date_joined": "2024-01-15T10:30:00Z"
}
```

**DELETE** `/users/{id}/`

Delete user by ID.

**Response (204):**
```
No content
```

### Expense Management

**GET** `/categories/`

Get all expense categories.

**Response (200):**
```json
[
    {
        "id": 1,
        "name": "Food"
    },
    {
        "id": 2,
        "name": "Travel"
    },
    {
        "id": 3,
        "name": "Entertainment"
    }
]
```

**POST** `/categories/`

Create a new category.

**Request Body:**
```json
{
    "name": "Shopping"
}
```

**GET** `/expenses/`

Get all expenses.

**Response (200):**
```json
[
    {
        "id": 1,
        "title": "Lunch at restaurant",
        "amount": "25.50",
        "category": 1,
        "category_name": "Food",
        "date": "2024-01-15",
        "user": 1
    }
]
```

**POST** `/expenses/`

Create a new expense.

**Request Body:**
```json
{
    "title": "Movie tickets",
    "amount": "15.00",
    "category": 3,
    "date": "2024-01-15"
}
```

**GET** `/expenses/summary/`

Get total expense amount grouped by category using Django ORM aggregation.

**Response (200):**
```json
{
    "Food": 1200.50,
    "Travel": 3000.00,
    "Entertainment": 800.25
}
```

## Database

The project uses SQLite by default (configured in `settings.py`). To use PostgreSQL:

1. Update `DATABASES` in `settings.py`
2. Install PostgreSQL and create a database
3. Update the database configuration



## Testing the API

You can test the API using:

1. **curl**
   ```bash
   # Register a user
   curl -X POST http://127.0.0.1:8000/register/ \
        -H "Content-Type: application/json" \
        -d '{"username": "testuser", "email": "test@example.com", "password": "password123", "password_confirm": "password123"}'
   
   # Get all users
   curl http://127.0.0.1:8000/users/
   
   # Get expense summary
   curl http://127.0.0.1:8000/expenses/summary/
   ```

2. **Django REST Framework Browsable API**
   Visit any endpoint in your browser to see the interactive API interface.

## Validation Rules

### User Registration
- **Username**: Minimum 5 characters, must be unique
- **Email**: Valid email format, must be unique
- **Password**: Minimum 8 characters, must contain at least one number
- **Password Confirmation**: Must match password

### Expense
- **Title**: Required string field
- **Amount**: Decimal field with max 10 digits and 2 decimal places
- **Category**: Foreign key to Category model
- **Date**: Date field
- **User**: Foreign key to User model (automatically assigned)

## Technologies Used

- **Django 5.2.7**: Web framework
- **Django REST Framework 3.16.1**: API framework
- **SQLite**: Database (default)
- **PostgreSQL**: Alternative database (psycopg2-binary included)
- **Python 3.8+**: Programming language
