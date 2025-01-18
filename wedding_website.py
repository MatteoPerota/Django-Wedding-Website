from django.shortcuts import render
from django.http import HttpResponse

# views.py
def home(request):
    return render(request, 'home.html')

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

# settings.py (add this in the TEMPLATES setting)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# templates/home.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Martina & Matteo's Wedding</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: url('BigWallpaper.jpg') no-repeat center center fixed;
            background-size: cover;
        }

        .head-banner {
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 20px;
            text-align: center;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .head-banner h1 {
            margin: 0;
            font-size: 2.5em;
        }

        .head-banner nav {
            margin-top: 10px;
        }

        .head-banner nav a {
            color: white;
            margin: 0 15px;
            text-decoration: none;
            font-size: 1.2em;
        }

        .head-banner nav a:hover {
            text-decoration: underline;
        }

        .rsvp-button {
            display: inline-block;
            margin: 20px auto;
            padding: 10px 20px;
            font-size: 1.2em;
            background-color: #ff6347;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
        }

        .rsvp-button:hover {
            background-color: #e5533d;
        }
    </style>
</head>
<body>
    <div class="head-banner">
        <h1>Martina & Matteo</h1>
        <nav>
            <a href="#date-time">Date & Times</a>
            <a href="#location">Location</a>
            <a href="#faqs">FAQs</a>
        </nav>
    </div>

    <div style="text-align: center; margin-top: 50px;">
        <a href="#rsvp" class="rsvp-button">RSVP</a>
    </div>
</body>
</html>

# static/images/couple_photo.jpg
# (Add your photo in the 'static/images' folder and name it as couple_photo.jpg)

# Runserver
# Make sure you have set up static files correctly in settings.py and collected static files.
# Command to run the server:
# python manage.py runserver
