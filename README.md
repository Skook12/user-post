# Python Clean Code API

A clean architecture REST API built with Python and Flask, implementing user management functionality following SOLID principles and clean code practices.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [API Documentation](#api-documentation)
- [Database Schema](#database-schema)
- [Testing](#testing)
- [Development Guidelines](#development-guidelines)
- [Error Handling](#error-handling)
- [Contributing](#contributing)

## 🎯 Overview

This project demonstrates a well-structured Python API following Clean Architecture principles. It provides endpoints for user management with proper separation of concerns, dependency injection, and comprehensive error handling.

### Key Principles Implemented

- **Clean Architecture**: Clear separation between layers (controllers, models, views, repositories)
- **SOLID Principles**: Single responsibility, dependency inversion, interface segregation
- **Dependency Injection**: Using composition over inheritance
- **Interface-based Design**: Abstract interfaces for better testability
- **Error Handling**: Comprehensive error management with custom exception types

## 🏗️ Architecture

The project follows a layered architecture pattern:

```
┌─────────────────────────────────────┐
│            Routes Layer             │  ← HTTP endpoints
├─────────────────────────────────────┤
│            Views Layer              │  ← Request/Response handling
├─────────────────────────────────────┤
│          Controllers Layer          │  ← Business logic
├─────────────────────────────────────┤
│         Repositories Layer          │  ← Data access
├─────────────────────────────────────┤
│           Models Layer              │  ← Database entities
└─────────────────────────────────────┘
```

### Architecture Components

1. **Routes** (`src/main/routes/`): Define HTTP endpoints and route handlers
2. **Views** (`src/views/`): Handle HTTP request/response formatting
3. **Controllers** (`src/controllers/`): Contain business logic
4. **Repositories** (`src/models/repositories/`): Handle data persistence
5. **Models** (`src/models/entities/`): Define database entities
6. **Composers** (`src/main/composer/`): Dependency injection and object composition

## ✨ Features

- **User Creation**: Create new users with validation
- **User Search**: Find users by name
- **Data Validation**: Input validation using Pydantic
- **Error Handling**: Comprehensive error management
- **Database Operations**: SQLite database with SQLAlchemy ORM
- **Testing**: Unit tests with pytest
- **Clean Code**: Following PEP 8 and clean code principles

## 🛠️ Technology Stack

- **Python 3.12+**
- **Flask 3.1.2** - Web framework
- **SQLAlchemy 2.0.43** - ORM for database operations
- **Pydantic 2.11.9** - Data validation
- **pytest 8.4.2** - Testing framework
- **SQLite** - Database (with schema initialization)

## 📁 Project Structure

```
api/
├── src/
│   ├── controllers/           # Business logic layer
│   │   ├── interfaces/        # Abstract interfaces
│   │   ├── user_creator.py    # User creation logic
│   │   ├── user_finder.py     # User search logic
│   │   └── *_test.py          # Controller tests
│   ├── errors/                # Error handling
│   │   ├── error_handler.py   # Centralized error handling
│   │   └── error_types/       # Custom exception types
│   ├── main/                  # Application entry point
│   │   ├── composer/          # Dependency injection
│   │   ├── routes/            # HTTP routes
│   │   └── server/            # Flask app configuration
│   ├── models/                # Data layer
│   │   ├── connection/        # Database connection
│   │   ├── entities/          # Database models
│   │   └── repositories/      # Data access layer
│   ├── validators/            # Input validation
│   └── views/                 # HTTP request/response handling
│       ├── http_types/        # Request/Response models
│       ├── user_creator_view.py
│       └── user_finder_view.py
├── init/                      # Database initialization
│   └── schema.sql            # Database schema
├── requirements.txt          # Python dependencies
├── run.py                    # Application entry point
└── schema.db                # SQLite database file
```

## 🚀 Setup Instructions

### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd api
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize database**
   ```bash
   # The database will be automatically created when you run the application
   # Schema is defined in init/schema.sql
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

   The API will be available at `http://localhost:3000`

## 📚 API Documentation

### Base URL
```
http://localhost:3000
```

### Endpoints

#### 1. Create User
**POST** `/user`

Creates a new user in the system.

**Request Body:**
```json
{
    "person_name": "John Doe",
    "age": 30,
    "height": 1.75
}
```

**Validation Rules:**
- `person_name`: Required, minimum 3 characters
- `age`: Required, integer
- `height`: Required, float

**Success Response (200):**
```json
{
    "Type": "Users",
    "count": 1,
    "message": "User created successfully"
}
```

**Error Responses:**
- **400 Bad Request**: User already exists
- **422 Unprocessable Entity**: Validation errors

#### 2. Find User
**GET** `/user/find/{person_name}`

Searches for users by name.

**Path Parameters:**
- `person_name`: Name of the user to search for

**Success Response (200):**
```json
{
    "Type": "Users",
    "count": 1,
    "users": [
        {
            "id": 1,
            "person_name": "John Doe",
            "age": 30,
            "height": 1.75
        }
    ]
}
```

**Error Responses:**
- **404 Not Found**: User not found

### Example Usage

```bash
# Create a new user
curl -X POST http://localhost:3000/user \
  -H "Content-Type: application/json" \
  -d '{
    "person_name": "Jane Smith",
    "age": 25,
    "height": 1.68
  }'

# Find a user
curl http://localhost:3000/user/find/Jane%20Smith
```

## 🗄️ Database Schema

The application uses SQLite with the following schema:

```sql
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_name TEXT NOT NULL,
    age INTEGER,
    height REAL
);
```

**Table: `users`**
- `id`: Primary key, auto-incrementing integer
- `person_name`: User's name (required, text)
- `age`: User's age (optional, integer)
- `height`: User's height (optional, real number)

## 🧪 Testing

The project includes comprehensive unit tests using pytest.

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest src/controllers/user_creator_test.py
```

### Test Structure

Tests are organized with:
- **Mock objects** for repository dependencies
- **Unit tests** for controllers
- **Error handling tests** for various scenarios
- **Validation tests** for input data

### Example Test

```python
def test_insert_new_user():
    user_repository = UserRepositoryMock()
    user_creator = UserCreator(user_repository)
    
    response = user_creator.insert_new_user("John Doe", 30, 1.75)
    
    assert response["Type"] == "Users"
    assert response["count"] == 1
```

## 💡 Development Guidelines

### Code Organization

1. **Controllers**: Handle business logic and orchestrate operations
2. **Repositories**: Abstract data access layer
3. **Views**: Handle HTTP request/response formatting
4. **Models**: Define data structures and database entities
5. **Validators**: Handle input validation using Pydantic

### Coding Standards

- Follow **PEP 8** style guidelines
- Use **type hints** for better code documentation
- Implement **interfaces** for better testability
- Keep **functions small** and focused on single responsibility
- Use **meaningful variable names** and comments

### Adding New Features

1. **Define Interface**: Create abstract interface in `interfaces/`
2. **Implement Controller**: Add business logic in `controllers/`
3. **Create Repository**: Implement data access in `repositories/`
4. **Add View**: Handle HTTP in `views/`
5. **Create Composer**: Wire dependencies in `composer/`
6. **Add Routes**: Define endpoints in `routes/`
7. **Write Tests**: Add unit tests for new functionality

## ⚠️ Error Handling

The application implements a comprehensive error handling system:

### Error Types

1. **HttpBadRequestError (400)**: Invalid request data
2. **HttpNotFoundError (404)**: Resource not found
3. **HttpUnprocessableEntityError (422)**: Validation errors

### Error Response Format

```json
{
    "error": [
        {
            "title": "ErrorType",
            "detail": "Error message description"
        }
    ]
}
```

### Centralized Error Handling

All errors are handled by the `error_handler.py` module, ensuring consistent error responses across the application.

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-feature`
3. **Make changes** following the coding standards
4. **Add tests** for new functionality
5. **Run tests** to ensure everything works
6. **Commit changes**: `git commit -m "Add new feature"`
7. **Push to branch**: `git push origin feature/new-feature`
8. **Create a Pull Request**

### Development Workflow

1. Follow the existing architecture patterns
2. Write tests for all new functionality
3. Update documentation for API changes
4. Ensure all tests pass before submitting PR
5. Use meaningful commit messages

## 📝 License

This project is for educational purposes, demonstrating clean code practices and clean architecture principles in Python.

---

**Built with ❤️ following Clean Architecture principles**
