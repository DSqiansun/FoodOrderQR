from django.urls import path
from OrderApp.views import index,orderV


urlpatterns=[
    path('',index,name='index'),
    path('orders/<str:tableid>',orderV,name='order'),

]