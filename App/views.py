import os
import random
import time
import uuid
import hashlib

from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.models import Wheel, Nav, Mustbuy, Shop, MainShow, Foodtypes, Goods, User, Cart, Order, OrderGoods
from Axf import settings


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
    token = request.session.get('token')
    if token:
        user = User.objects.get(token=token)
        carts = Cart.objects.filter(user=user).exclude(number=0)
        return render(request, 'cart/cart.html', context={'carts': carts})
    else:
        return redirect('App:login')


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
    token = request.session.get('token')
    carts = []
    if token:
        user = User.objects.get(token=token)
        carts = Cart.objects.filter(user=user)
    data = {
        'foodtypes':foodtypes,
        'goodslist':goodslist,
        'childTypleList':childTypleList,
        'categoryid':categoryid,
        'childid':childid,
        'carts':carts
    }
    return render(request,'market/market.html',context=data)


def mine(request):
    token = request.session.get('token')
    responseData = {}
    if token:
        user = User.objects.get(token=token)
        responseData['name'] = user.name
        responseData['rank'] = user.rank
        responseData['img'] = '/static/uploads/' + user.img
        responseData['isLogin'] = 1
    else:
        responseData['name'] = '未登录'
        responseData['img'] = '/static/uploads/axf.png'
    return render(request, 'mine/mine.html', context=responseData)


def genarate_password(param):
    sha = hashlib.sha256()
    sha.update(param.encode('utf-8'))
    return sha.hexdigest()


def registe(request):
    if request.method == 'GET':
        return render(request, 'mine/registe.html')
    elif request.method == 'POST':
            user = User()
            user.account = request.POST.get('account')
            user.password = genarate_password(request.POST.get('password'))
            user.name = request.POST.get('name')
            user.tel = request.POST.get('tel')
            user.addr = request.POST.get('addr')
            imgName = user.account + '.png'
            imagePath = os.path.join(settings.MEDIA_ROOT, imgName)
            file = request.FILES.get('icon')
            with open(imagePath, 'wb') as fp:
                for data in file.chunks():
                    fp.write(data)
            user.img = imgName
            user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))
            user.save()
            request.session['token'] = user.token
            return redirect('App:mine')


def checkaccount(request):
    account = request.GET.get('account')
    responseData = {
        'msg': '账号可用',
        'status': 1
    }
    try:
        user = User.objects.get(account=account)
        responseData['msg'] = '账号已被占用'
        responseData['status'] = -1
        return JsonResponse(responseData)
    except:
        return JsonResponse(responseData)


def login(request):
    if request.method == 'GET':
        return render(request, 'mine/login.html')
    elif request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        try:
            user = User.objects.get(account=account)
            if user.password == genarate_password(password):
                user.token = str(uuid.uuid5(uuid.uuid4(), 'login'))
                user.save()
                request.session['token'] = user.token
                return redirect('App:mine')
            else:
                return render(request, 'mine/login.html', context={'passwdErr': '密码错误!'})
        except:
            return render(request, 'mine/login.html', context={'acountErr':'账号不存在!'})


def logout(request):
    request.session.flush()
    return redirect('App:mine')

def addcart(request):
    goodsid = request.GET.get('goodsid')
    token = request.session.get('token')
    responseData = {
        'msg':'添加购物车成功',
        'status': 1
    }
    if token:
        user = User.objects.get(token=token)
        goods = Goods.objects.get(pk=goodsid)
        carts = Cart.objects.filter(user=user).filter(goods=goods)
        if carts.exists():
            cart = carts.first()
            cart.number = cart.number + 1
            cart.save()
            responseData['number'] = cart.number
        else:
            cart = Cart()
            cart.user = user
            cart.goods = goods
            cart.number = 1
            cart.save()
            responseData['number'] = cart.number
        return JsonResponse(responseData)
    else:
        responseData['msg'] = '未登录，请登录后操作'
        responseData['status'] = -1
        return JsonResponse(responseData)

def subcart(request):
    token = request.session.get('token')
    goodsid = request.GET.get('goodsid')
    user = User.objects.get(token=token)
    goods = Goods.objects.get(pk=goodsid)
    cart = Cart.objects.filter(user=user).filter(goods=goods).first()
    cart.number = cart.number - 1
    cart.save()
    responseData = {
        'msg': '购物车减操作成功',
        'status': 1,
        'number': cart.number
    }
    return JsonResponse(responseData)


def changecartstatus(request):
    cartid = request.GET.get('cartid')
    cart = Cart.objects.get(pk=cartid)
    cart.isselect = not cart.isselect
    cart.save()
    responseData = {
        'msg': '选中状态改变',
        'status': 1,
        'isselect': cart.isselect
    }
    return JsonResponse(responseData)


def changecartselect(request):
    isselect = request.GET.get('isselect')
    if isselect == 'true':
        isselect = True
    else:
        isselect = False
    token = request.session.get('token')
    user = User.objects.get(token=token)
    carts = Cart.objects.filter(user=user)
    for cart in carts:
        cart.isselect = isselect
        cart.save()
    return JsonResponse({'msg': '反选操作成功', 'status': 1})


def generateorder(request):
    token = request.session.get('token')
    user = User.objects.get(token=token)
    order = Order()
    order.user = user
    order.identifier = str(int(time.time())) + str(random.randrange(10000, 100000))
    order.save()
    carts = Cart.objects.filter(user=user).filter(isselect=True)
    for cart in carts:
        orderGoods = OrderGoods()
        orderGoods.order = order
        orderGoods.goods = cart.goods
        orderGoods.number = cart.number
        orderGoods.save()
        cart.delete()
    responseData = {
        'msg': '订单生成成功',
        'status': 1,
        'identifier': order.identifier
    }

    return JsonResponse(responseData)


def orderinfo(request, identifier):
    order = Order.objects.get(identifier=identifier)
    return render(request, 'order/orderinfo.html', context={'order':order})