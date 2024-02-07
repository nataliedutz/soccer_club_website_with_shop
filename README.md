# Soccer club website including a shop

## Overview
The goal of this ongoing project is to create a soccer club website including a shop.

## Development Setup

Before you begin, ensure you have met the following requirements:

- **Python:** This project is developed using Python 3.10.12. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

- **Integrated Development Environment (IDE):**
This entire application is built using Visual Studio Code.

- **Virtual Environment (Optional, but recommended):** It's a good practice to use a virtual environment for Python projects. You can create one using the `venv` module or `virtualenv`.
Open a terminal and navigate to the project directory. Use the command:
```
On Windows    : python -m venv venv
On macOS/Linux: python3 -m venv venv
```

- **Activate the virtual environment:**
```
On Windows    : .\venv\Scripts\activate
On macOS/Linux: source venv/bin/activate
```

- **Install Dependencies:**
```
On Windows    : pip install -r requirements.txt
On macOS/Linux: pip3 install -r requirements.txt
```

- **Navigate to the outer Django project directory in your terminal and run the project from here.**


## Project Execution

- **Database Settings:**
- You can use the default SQLite3, or you can choose Postgres. The information about database can be found in the file delivery_fee_calculator/settings.py.
- For Postgres you need to make neccessary changes for the fields NAME, USER, PASSWORD, HOST and PORT according to your database credentials.

```
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'xxxxxx', # Provide your database name
         'USER': 'xxxxxx', # Provide your database username
         'PASSWORD': 'xxxxxx', # Provide your database password
         'HOST': 'localhost', # Provide your database host 
         'PORT': '5432', # Provide your database port      
     }
 }
```

- **Run Migrations to create the database table from fee_calculator/models.py:**
```
On Windows    : python manage.py makemigrations 
                python manage.py migrate
On macOS/Linux: python3 manage.py makemigrations 
                python3 manage.py migrate
```

- **Start the Development Server:**
    
```
On Windows    : python manage.py runserver
On macOS/Linux: python3 manage.py runserver
```
