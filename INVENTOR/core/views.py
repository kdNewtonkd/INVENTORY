from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'dashbaord/index.html')
def staff(request):
    return render(request,'dashbaord/staff.html')

def product(request):
    return render(request,'dashbaord/product.html')

def order(request):
    return render(request,'dashbaord/order.html')