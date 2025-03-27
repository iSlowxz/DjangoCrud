# Django CRUD Application

A CRUD (Create, Read, Update, Delete) web application built with Django framework, Python, and MySQL database.

## Table of Contents
- [About](#about)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Members](#members)

## About
This project is a web-based CRUD application that allows users to perform basic Create, Read, Update, and Delete operations. Built using Django framework with MySQL as the database backend.

## Features
- Create new records
- Read/View existing records
- Update existing records
- Delete records
- Responsive web interface
- MySQL database integration

## Technologies Used
- Python 3.x
- Django Framework
- MySQL Database
- HTML/CSS
- Bootstrap

## Getting Started
### Prerequisites
- Python 3.x
- MySQL Server
- pip (Python package manager)

### Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/django-crud-mysql.git
cd django-crud-mysql
```

2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

4. Configure MySQL Database
```python
# In settings.py
'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangodb',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
```

5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Start the development server
```bash
python manage.py runserver
```

7. Visit `http://localhost:8000` in your web browser

## Members
- Mark Angelo Cornejo 
- Raphael Vinch Dulatre

## API Endpoints
- `GET /api/items/` - List all items
- `POST /api/items/` - Create a new item
- `GET /api/items/<id>/` - Retrieve a specific item
- `PUT /api/items/<id>/` - Update a specific item
- `DELETE /api/items/<id>/` - Delete a specific item 