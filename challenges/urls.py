from django.urls import path
# The dot (.) is used because we want to import 'views.py' from the same folder
from . import views

# Define URL patterns for the application
urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_number),
    # Access the 'monthly_chalange' function inside 'views' in this path ('/<month>')
    path("<str:month>", views.monthly_challenge)
]