from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
# Create your views here.
@login_required
def index(request):
    return render(request,'dashbaord/index.html')

@login_required
def staff(request):
    return render(request,'dashbaord/staff.html')

@login_required
def product(request):
    #items=Product.objects.all()
    items=Product.objects.raw('SELECT * FROM core_product')
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form=ProductForm()    
    context={
        'items':items,
        'form':form
    }
    return render(request,'dashbaord/product.html',context)

@login_required
def order(request):
    return render(request,'dashbaord/order.html')


def delete_product(request,pk):
    item=Product.objects.get(pk=pk)
   
    if request.method=='POST':
        item.delete()
        return redirect('product')
    return render(request,'dashbaord/delete.html')

#chagpt
#def delete_product(request, pk):
   # item = Product.objects.get(pk=pk)  # Correction : spécifier pk=pk
   
    #if request.method == 'POST':
       # item.delete()
       # return redirect('product')
    #return render(request, 'dashbaord/delete.html')  # Correction : utiliser la fonction render
 #item=Product.objects.raw('SELECT * FROM core_product WHERE id = pk')
def update_product(request, pk):
    item = Product.objects.get(pk=pk)
    if request.method=='POST':
        form=ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form=ProductForm(instance=item)    
    context={
        
        'form':form
    }
    return render(request,'dashbaord/update.html',context)