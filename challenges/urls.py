from django.urls import path
# The dot (.) is used because we want to import 'views.py' from the same folder
from . import views

# Define URL patterns for the application
urlpatterns = [
    # Access the 'index' function inside 'views' in this path ('/january')
    path("january", views.index)
]