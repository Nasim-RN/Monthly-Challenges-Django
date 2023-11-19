from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Hydration Challenge: Drink at least 8 glasses of water every day!",
    "february": "Mindful Eating: Practice mindful eating for all your meals.",
    "march": "Daily Exercise: Include 30 minutes of physical activity each day.",
    "april": "Quality Sleep: Aim for 7-9 hours of quality sleep every night.",
    "may": "Fruit and Veggie Feast: Consume a variety of fruits and vegetables daily.",
    "june": "Sugar-Free Month: Limit added sugars in your diet.",
    "july": "Mental Health Boost: Take 10 minutes daily for relaxation or mindfulness.",
    "august": "No-Soda Challenge: Eliminate sodas and sugary drinks from your diet.",
    "september": "Whole Grain Adventure: Choose whole grains over refined grains.",
    "october": "Plank Challenge: Increase core strength with daily planks.",
    "november": "Gratitude Journal: Write down three things you're grateful for each day.",
    "december": "Random Acts of Kindness: Perform one daily random act of kindness."
}


# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"
        # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."


    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported!")