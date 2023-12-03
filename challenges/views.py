from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from typing import List
from django.template.loader import render_to_string



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
    "december": None #"Random Acts of Kindness: Perform one daily random act of kindness."
}


# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenges_by_number(request, month: int):
    months: List[str] = monthly_challenges.keys()

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html",{
            "text":challenge_text,
            "month_name": month
        })

    except:
        raise Http404()