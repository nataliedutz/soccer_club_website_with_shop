SETUP
======

1 - Create a folder that you will keep your project

2 - Create a virtual environment

    Windows: python -m venv .venv

    Linux: python3 -m venv .venv

3 - Activate the venv
    
    a. Through the CLI
       Win: .venv/Scripts/Activate
       Lin: source .venv/bin/activate

    b. Open a new terminal (VS Code detects automatically the venv)

    c. Ctrl + Shift + P - Python: Select Interpreter - Select the .venv

4 - Install Django

    pip install django
    
PROJECT CREATION
================

1 - Create Project

django-admin startproject django_project .

(Note:  without . another top folder will be created with the same name)

2 - Have a check that everything is functioning properly

    Win: python manage.py runserver
    Lin: python3 manage.py runserver

3 - Open a browser and visit: http://127.0.0.1:8000/

4 - Ctrl + C stop the server

VS CODE setup for Django (Optional)
========================

In order to debug or run directly the Django app 
we create a launch.json file by going to Run and Debug tab
and then select create launch.json -> Python -> Django


5 - Create an application

    Win: python manage.py startapp pages
    Lin: python3 manage.py startapp pages
    
6 - Makemigrations - apply migrations

    These are necessary operations to the database
    Django can use many DB - if not specified otherwise sqlite3

    Django prepares data for the database but it is up to developper to apply

    Win: python manage.py migrate
    Lin: python3 manage.py migrate

7 - Add the newly created application named pages to the project settings.py file in  INSTALLED_APPS list.

    Here the name "pages" can be added as the last entry, but for application specific configuration
    we shall enter the entry "pages.apps.PagesConfig"

8 - Create a function as a view in pages.views.py 

    from django.http import HttpResponse

    def homePageView(request):
        return HttpResponse("Hello, World!")

9 - Route the request with empty path to this view in order to act as the home page

    Add ih the project urls.py file the second line as below
    Remember to import also the function view

    from pages.views import homePageView

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", homePageView),
    ]

10 - Run the server and test your home page!


PASSING DATA TO THE VIEWS
===========================

1 - First mechanism is to pass data as part of the url

    a - include in the urls.py file a pattern matching to /../<argname>/
    b - create a view that gets the argname as a second argument

    Type designators can also be applied to differentiate between different types

    HINT: Int type argument should be placed above str in the urlpattern list
        because otherwise int is parsed to str automatically

2 - Using the http protocol to pass data according to the http method (get, post, ...)
    These two methods pass data in a different way.

    a - get method - passes data to the url with the ? syntax like ?arg1=val1&arg2=val2&...

        we can get this data in our view by using the request object

    b - post method