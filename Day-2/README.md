# 🌐 WITER PEP – Day 2 (Django Web Development)

This repository contains a Django web application built during the WITER PEP Session – Day 2.
The focus is on understanding Django fundamentals, creating models, views, URL routing, and building a basic polling application.

## 📌 Topics Covered

- Django Project Setup
- Django Apps and Modularity
- Models and Database Design
- Views and Request Handling
- URL Routing and Path Mapping
- Admin Interface
- Database Migrations
- HTTP Responses

## 🚀 Project Overview

This is a **Polling Application** built with Django that allows users to create polls and cast votes.

### Project Structure

```
myproject/          # Django project configuration
├── __init__.py
├── asgi.py        # ASGI configuration
├── wsgi.py        # WSGI configuration
├── settings.py    # Project settings
└── urls.py        # Main URL router

polls/              # Django app for polling functionality
├── __init__.py
├── models.py      # Database models
├── views.py       # View logic
├── urls.py        # App-specific URL routing
├── admin.py       # Admin interface configuration
├── apps.py        # App configuration
├── tests.py       # Unit tests
└── migrations/    # Database migration files

manage.py           # Django management CLI
db.sqlite3          # SQLite database file
```

## 📊 Database Models

### Question Model
```python
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
```

- **question_text**: The text of the poll question (max 200 characters)
- **pub_date**: Timestamp when the question was published

### Choice Model
```python
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

- **question**: Foreign key relationship to Question (one-to-many)
- **choice_text**: The text of the choice option (max 200 characters)
- **votes**: Number of votes for this choice (default: 0)

### 📌 Key Concepts

- **ForeignKey**: Creates a many-to-one relationship
- **CASCADE**: Deletes associated choices when a question is deleted
- **DateTimeField**: Stores date and time information
- **CharField**: Stores text data with a maximum length
- **IntegerField**: Stores integer values

## 🔄 URL Routing

### Main Project URLs (`myproject/urls.py`)
```python
urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

### App URLs (`polls/urls.py`)
```python
urlpatterns = [
    path("", views.index, name="index"),
]
```

**Accessible at:** `http://localhost:8000/polls/`

## 👀 Views

### Index View (`polls/views.py`)
```python
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

- Returns a simple HTTP response
- Serves as the entry point for the polls application
- Can be extended to display all available polls

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8+
- Django 3.2+ (or specified version in requirements.txt)

### Installation

1. **Create and activate virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install Django:**
```bash
pip install django
```

3. **Run migrations:**
```bash
python manage.py migrate
```

4. **Create superuser (for admin access):**
```bash
python manage.py createsuperuser
```

5. **Start development server:**
```bash
python manage.py runserver
```

6. **Access the application:**
- Polls App: `http://localhost:8000/polls/`
- Admin Panel: `http://localhost:8000/admin/`

## 🔧 Useful Django Commands

| Command | Description |
|---------|-------------|
| `python manage.py runserver` | Start development server |
| `python manage.py migrate` | Apply database migrations |
| `python manage.py makemigrations` | Create migration files from model changes |
| `python manage.py shell` | Open interactive Python shell with Django context |
| `python manage.py createsuperuser` | Create admin user |
| `python manage.py collectstatic` | Collect static files for production |

## 📚 Key Django Concepts

### Models
- Define database schema using Python classes
- Automatically create database tables
- Provide ORM (Object-Relational Mapping) for database queries

### Views
- Handle HTTP requests and return responses
- Can render HTML templates or return JSON/HTTP responses
- Contains business logic

### URLs
- Map URL patterns to views
- Support dynamic parameters in URLs
- Allow named URL patterns for reverse lookups

### Admin Interface
- Automatically generated admin panel
- Register models to manage them through UI
- Built-in CRUD (Create, Read, Update, Delete) operations

### Migrations
- Track database schema changes
- Allow version control of database state
- Enable rollback to previous states

## 📈 Learning Outcomes

- ✅ Understand Django project structure
- ✅ Create and configure Django apps
- ✅ Define database models with relationships
- ✅ Implement views and URL routing
- ✅ Work with the Django admin interface
- ✅ Execute database migrations
- ✅ Handle HTTP requests and responses


## 📅 Session Info

| Attribute | Value |
|-----------|-------|
| Program   | WITER PEP |
| Day       | 2 |
| Framework | Django |
| Database  | SQLite3 |
| Python Version | 3.8+ |

## 🔗 Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Models Reference](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django Views Reference](https://docs.djangoproject.com/en/stable/topics/http/views/)
- [Django URL Dispatcher](https://docs.djangoproject.com/en/stable/topics/http/urls/)