from django.shortcuts import render
from OrderApp.form import FoodList
from OrderApp.models import FooditemsModel
# Create your views here.
def index(request):

    return render(request,'OrderApp/index.html')

def orderV(request,tableid):

    if request.POST:
        form = FoodList(request.POST)
        if form.is_valid():
            objj =FooditemsModel(
                itemname = form.cleaned_data['item_name'],table_id=tableid)
            objj.save()

    context={
        'formm':FoodList,
        'tableid':tableid

    }
    return render(request,'OrderApp/cart.html',context)