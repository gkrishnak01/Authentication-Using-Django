Add a secret key in settings.py
This is a sample program for an authentication app in a django project.
To add this app to your project:
    Copy Authentication to your project
    Add Authentication to the installed apps in settings.py file
    Add files from templates folder to templates folder( or its alternative in your project)
    Import "include" from django.urls to urls.py
    Add path('', include('Authentication.urls')) to urls.py