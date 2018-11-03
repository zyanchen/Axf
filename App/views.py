from django.shortcuts import render

# Create your views here.
from App.models import Wheel, Nav, Mustbuy, Shop, MainShow, Foodtypes, Goods


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


def market(request,categoryid,childid,sortid):

    foodtypes = Foodtypes.objects.all()

    typeIndex = int(request.COOKIES.get('typeIndex', 0))
    categoryid = foodtypes[typeIndex].typeid

    childtypenames = foodtypes.get(typeid=categoryid).childtypenames


    childTypleList = []
    for item in childtypenames.split('#'):
        arr = item.split(':')
        dir = {
            'childname':arr[0],
            'childid':arr[1],
        }
        childTypleList.append(dir)

    if childid == '0':
        goodslist = Goods.objects.filter(categoryid=categoryid)
    else:
        goodslist = Goods.objects.filter(categoryid=categoryid, childcid=childid)

    if sortid == '1':
        goodslist = goodslist.order_by('-productnum')
    elif sortid == '2':
        goodslist = goodslist.order_by('price')
    elif sortid == '3':
        goodslist = goodslist.order_by('-price')



    data = {
        'foodtypes':foodtypes,
        'goodslist':goodslist,
        'childTypleList':childTypleList,
        'categoryid':categoryid,
        'childid':childid,

    }
    return render(request,'market/market.html',context=data)


def mine(request):
    return render(request,'mine/mine.html')