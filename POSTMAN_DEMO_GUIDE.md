# Complete Postman Demo Guide - Django REST API

## 🚀 **Step 1: Start Your Django Server**

### **Terminal Commands:**
```bash
cd /home/abhijith/Documents/SanjayPP
source venv/bin/activate
python manage.py runserver
```

**Expected Output:**
```
Watching for file changes with StatReloader
Performing system checks...
System check identified no issues (0 silenced).
October 09, 2025 - 10:30:00
Django version 5.2.7, using settings 'machine_test_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

---

## 📋 **Step 2: Create Postman Collection**

### **2.1 Create New Collection**
1. Open Postman
2. Click "New" → "Collection"
3. Name: `Django Machine Test API`
4. Description: `Django REST API with User Management and Expense Tracking`

### **2.2 Create Environment**
1. Click "Environments" → "Create Environment"
2. Name: `Django Local`
3. Add Variables:
   - `base_url`: `http://127.0.0.1:8000`
   - `user_id`: `1`
   - `category_id`: `1`

---

## 🧪 **Step 3: API Testing - User Management**

### **3.1 User Registration (Valid Data)**

**Request Setup:**
- **Method**: `POST`
- **URL**: `{{base_url}}/register/`
- **Headers**:
  ```
  Content-Type: application/json
  ```
- **Body** (raw JSON):
  ```json
  {
      "username": "john_doe",
      "email": "john@example.com",
      "password": "password123",
      "password_confirm": "password123"
  }
  ```

**Expected Response (201 Created):**
```json
{
    "message": "User registered successfully",
    "user": {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com",
        "date_joined": "2025-10-09T10:30:00.000000Z"
    }
}
```

### **3.2 User Registration (Validation Errors)**

**Request Setup:**
- **Method**: `POST`
- **URL**: `{{base_url}}/register/`
- **Headers**:
  ```
  Content-Type: application/json
  ```
- **Body** (raw JSON):
  ```json
  {
      "username": "ab",
      "email": "invalid-email",
      "password": "short",
      "password_confirm": "different"
  }
  ```

**Expected Response (400 Bad Request):**
```json
{
    "message": "Registration failed",
    "errors": {
        "username": [
            "Ensure this field has at least 5 characters."
        ],
        "email": [
            "Enter a valid email address."
        ],
        "password": [
            "Ensure this field has at least 8 characters."
        ]
    }
}
```

### **3.3 Get All Users**

**Request Setup:**
- **Method**: `GET`
- **URL**: `{{base_url}}/users/`

**Expected Response (200 OK):**
```json
[
    {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com",
        "date_joined": "2025-10-09T10:30:00.000000Z"
    }
]
```

### **3.4 Get User by ID**

**Request Setup:**
- **Method**: `GET`
- **URL**: `{{base_url}}/users/{{user_id}}/`

**Expected Response (200 OK):**
```json
{
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "date_joined": "2025-10-09T10:30:00.000000Z"
}
```

### **3.5 Delete User**

**Request Setup:**
- **Method**: `DELETE`
- **URL**: `{{base_url}}/users/{{user_id}}/`

**Expected Response (204 No Content):**
```
(Empty body)
```

---

## 💰 **Step 4: API Testing - Expense Management**

### **4.1 Get All Categories**

**Request Setup:**
- **Method**: `GET`
- **URL**: `{{base_url}}/categories/`

**Expected Response (200 OK):**
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

### **4.2 Create New Category**

**Request Setup:**
- **Method**: `POST`
- **URL**: `{{base_url}}/categories/`
- **Headers**:
  ```
  Content-Type: application/json
  ```
- **Body** (raw JSON):
  ```json
  {
      "name": "Healthcare"
  }
  ```

**Expected Response (201 Created):**
```json
{
    "id": 4,
    "name": "Healthcare"
}
```

### **4.3 Get All Expenses**

**Request Setup:**
- **Method**: `GET`
- **URL**: `{{base_url}}/expenses/`

**Expected Response (200 OK):**
```json
[
    {
        "id": 1,
        "title": "Lunch at restaurant",
        "amount": "25.50",
        "category": 1,
        "category_name": "Food",
        "date": "2025-10-09",
        "user": 1
    }
]
```

### **4.4 Create New Expense**

**Request Setup:**
- **Method**: `POST`
- **URL**: `{{base_url}}/expenses/`
- **Headers**:
  ```
  Content-Type: application/json
  ```
- **Body** (raw JSON):
  ```json
  {
      "title": "Doctor visit",
      "amount": "100.00",
      "category": 4,
      "date": "2025-10-09"
  }
  ```

**Expected Response (201 Created):**
```json
{
    "id": 2,
    "title": "Doctor visit",
    "amount": "100.00",
    "category": 4,
    "category_name": "Healthcare",
    "date": "2025-10-09",
    "user": 1
}
```

### **4.5 Expense Summary (Main Feature)**

**Request Setup:**
- **Method**: `GET`
- **URL**: `{{base_url}}/expenses/summary/`

**Expected Response (200 OK):**
```json
{
    "Food": 25.50,
    "Healthcare": 100.0,
    "Travel": 0.0,
    "Entertainment": 0.0
}
```

---

## 🎯 **Step 5: Complete Demo Flow**

### **5.1 Demo Script for Interviewers**

**Opening:**
> "Let me demonstrate this Django REST API I built. I'll start with an empty database and create data live using Postman."

**Step-by-Step Demo:**

1. **Show Empty State** (30 seconds)
   - GET `/users/` → `[]`
   - GET `/categories/` → `[]`
   - GET `/expenses/` → `[]`
   - GET `/expenses/summary/` → `{}`

2. **Create Categories** (30 seconds)
   - POST `/categories/` → "Food"
   - POST `/categories/` → "Travel"
   - POST `/categories/` → "Entertainment"

3. **Register Users** (1 minute)
   - POST `/register/` → Valid user
   - POST `/register/` → Show validation errors

4. **Create Expenses** (1 minute)
   - POST `/expenses/` → Multiple expenses
   - Show foreign key relationships

5. **Show Expense Summary** (30 seconds)
   - GET `/expenses/summary/`
   - Explain Django ORM aggregation

6. **User Management** (30 seconds)
   - GET `/users/`
   - GET `/users/1/`
   - DELETE `/users/1/`

### **5.2 Key Points to Highlight**

- **"Notice the validation working in real-time"**
- **"Here's Django ORM aggregation grouping expenses by category"**
- **"All relationships work - expenses linked to categories and users"**
- **"Proper HTTP status codes - 201 for creation, 400 for validation errors"**
- **"Clean JSON responses with proper error handling"**

---

## 📊 **Step 6: Postman Collection Export**

### **6.1 Export Collection**
1. Right-click collection → "Export"
2. Choose "Collection v2.1"
3. Save as `Django_Machine_Test_API.postman_collection.json`

### **6.2 Share with Interviewers**
- Email the collection file
- They can import it into Postman
- Shows professional API development practices

---

## 🚀 **Step 7: Advanced Postman Features**

### **7.1 Pre-request Scripts**
```javascript
// Set timestamp for unique data
pm.environment.set("timestamp", Date.now());
```

### **7.2 Test Scripts**
```javascript
// Extract user ID from response
if (pm.response.code === 201) {
    const response = pm.response.json();
    if (response.user && response.user.id) {
        pm.environment.set("user_id", response.user.id);
    }
}
```

### **7.3 Environment Variables Usage**
- `{{base_url}}/users/{{user_id}}/`
- `{{base_url}}/expenses/?user={{user_id}}`

---

## 💡 **Pro Tips for Interview**

1. **Organize Requests in Folders:**
   - User Management
   - Category Management
   - Expense Management
   - Validation Tests

2. **Use Descriptive Names:**
   - "Create Valid User"
   - "Show Validation Errors"
   - "Get Expense Summary"

3. **Add Request Descriptions:**
   - Explain what each endpoint does
   - Show expected responses
   - Highlight technical features

4. **Show Response Times:**
   - Postman displays request duration
   - Good for performance discussions

**Total Demo Time: 5-7 minutes**
**Perfect for technical interviews!** 🎉
