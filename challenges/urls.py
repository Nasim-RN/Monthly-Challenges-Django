from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # /challenges/
    path("<int:month>", views.monthly_challenges_by_number),
    # Access the 'monthly_chalange' function inside 'views' in this path ('/<month>')
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
