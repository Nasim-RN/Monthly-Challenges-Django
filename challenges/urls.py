from django.urls import path
# The dot (.) is used because we want to import 'views.py' from the same folder
from . import views

# Define URL patterns for the application
urlpatterns = [
    # Access the 'monthly_chalange' function inside 'views' in this path ('/<month>')
    path("<month>", views.monthly_challenge)
]