from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
@login_required
def index(request):
    orders=Order.objects.all()
    products=Product.objects.all()
    counts= User.objects.all().count()
    procount=Product.objects.all().count()
    order_count=Order.objects.all().count()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff=request.user
            instance.save()
            return redirect('index')
    else:
        form=OrderForm()    
    context={
        'orders':orders,
        'form':form,
        'products':products,
        'counts':counts,
        'procount':procount,
        'order_count':order_count
    }
    return render(request,'dashbaord/index.html',context)

@login_required
def staff(request):
    counts= User.objects.all().count()
    workers= User.objects.all()
    procount=Product.objects.all().count()
    order_count=Order.objects.all().count()
    context={
        'workers':workers,
        'counts':counts,
        'procount':procount,
        'order_count':order_count
    }
    return render(request,'dashbaord/staff.html',context)
@login_required
def product(request):
    items=Product.objects.all()
    #items=Product.objects.raw('SELECT * FROM core_product')
    counts= User.objects.all().count()
    procount=Product.objects.all().count()
    order_count=Order.objects.all().count()
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name=form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('product')
    else:
        form=ProductForm()    
    context={
        'items':items,
        'form':form,
        'counts':counts,
        'procount':procount,
        'order_count':order_count
    }
    return render(request,'dashbaord/product.html',context)

@login_required
def order(request):
    orders=Order.objects.all()
    counts= User.objects.all().count()
    procount=Product.objects.all().count()
    order_count=Order.objects.all().count()
    context={
        'orders':orders,
        'counts':counts,
        'procount':procount,
        'order_count':order_count
    }
    return render(request,'dashbaord/order.html',context)

@login_required
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
 
 
@login_required
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

@login_required
def staff_detail(request,pk):
    workers=User.objects.get(pk=pk)
    context={
        'workers':workers
    }
    return render(request,'dashbaord/staff_detail.html',context)