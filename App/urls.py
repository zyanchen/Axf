from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^market/$', views.market, name='market'),
    url(r'^mine/$', views.mine, name='mine'),

]