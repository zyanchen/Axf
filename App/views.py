from django.shortcuts import render

# Create your views here.
from App.models import Wheel, Nav, Mustbuy, Shop, MainShow, Foodtypes


def index(request):
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    musts = Mustbuy.objects.all()
    shoplist = Shop.objects.all()
    shophead = shoplist[0]
    shoptab = shoplist[1:3]
    shopclass = shoplist[3:7]
    shopcommend = shoplist[7:11]

    mainshows = MainShow.objects.all()

    data = {
        'wheels':wheels,
        'navs':navs,
        'musts':musts,
        'shophead':shophead,
        'shoptab':shoptab,
        'shopclass':shopclass,
        'shopcommend':shopcommend,
        'mainshows':mainshows,
    }
    return render(request,'home/home.html',context=data)


def cart(request):
    return render(request,'cart/cart.html')


def market(request):

    foodtypes = Foodtypes.objects.all()

    data = {
        'foodtypes':foodtypes,
    }

    return render(request,'market/market.html',context=data)


def mine(request):
    return render(request,'mine/mine.html')