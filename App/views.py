from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home/home.html')


def cart(request):
    return None


def market(request):
    return render(request,'market/market.html')


def mine(request):
    return None