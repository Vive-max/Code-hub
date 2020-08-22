from django.shortcuts import render
import django.http import HttpRasponce

# Create your views here.
def learn_django(Request):
    return HttpRasponce('hello Django')
