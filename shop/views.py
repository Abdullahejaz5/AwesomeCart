from django.shortcuts import render
from django.http import HttpResponse
from .models import Products, Contact,Order,Update
from math import ceil
import json
# Create your views here.
def verify(query,products):
    final_products=[]
    for product in products:
        if query.lower() in product.product_desc.lower() or query.lower() in product.product_name.lower() or query.lower() in product.product_category.lower():
            final_products.append(product)
    return final_products

def home (request):
    categories=Products.objects.values('product_category').distinct()
    prod=[]
    for category in categories:
        category=category['product_category']
        product=Products.objects.filter(product_category=category)
        
        l1 = len(product)
        slides = (l1 // 4) + ceil((l1 / 4) - (l1 // 4))
        range_1 = range(1, slides)
        a=[product,range_1]
        prod.append([product,range_1])
        print(slides)

    print(prod)
    return render(request,'shop/home.html',{'prod':prod})
def search (request):
    query=request.GET.get('Search','')
    prod=[]
    if len(query)>3:
        categories=Products.objects.values('product_category').distinct()
        for category in categories:
            category=category['product_category']
            temp_product=Products.objects.filter(product_category=category)
            product=verify(query,temp_product)
        
            l1 = len(product)
            if l1>0:
                slides = (l1 // 4) + ceil((l1 / 4) - (l1 // 4))
                range_1 = range(1, slides)
                a=[product,range_1]
                prod.append([product,range_1])
        
    if len(prod)>0:
        return render(request,'shop/search.html',{'prod':prod,'msg':False})
    else:
        return render(request,'shop/search.html',{'prod':prod,'msg':True})



def about (request):
    return render(request,'shop/about_us.html')
def contact (request):
    if request.method=='POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        contact=request.POST.get('contact','')
        message=request.POST.get('message','')
        comp_pack=Contact(name=name,email=email,contact=contact,message=message)
        thanks=True
        comp_pack.save()
        return render(request, 'shop/contact_us.html',{'thanks':thanks})

    return render(request, 'shop/contact_us.html')



def tracker (request):
    if request.method=='POST':
        email=request.POST.get('email','')
        order_id=request.POST.get('order_id',-1)
    
        
        
        try:
            order=Order.objects.filter(order_id=order_id,email=email)
            records=Update.objects.filter(order_id=order_id)
            product=json.loads(order[0].json_products)
            if len(records)!=0 and len(order)!=0:
                data=[]
                for record in records:
                    data.append({'update':record.order_status,'time':record.update_time})
               
                return(HttpResponse(json.dumps([data,product],default=str)))
            else:
                return(HttpResponse(json.dumps([])))
        except Exception as e:
            return(HttpResponse(json.dumps([])))
    
    return render(request,'shop/tracker.html')

def productview (request,myid):
    product=Products.objects.filter(id=myid)
    return render(request,'shop/product_view.html',{'product':product[0]})
def checkout (request):
    if request.method=='POST':
        name=request.POST.get('name','')
        price=request.POST.get('price','')

        email=request.POST.get('email','')
        contact=request.POST.get('contact','')
        address=request.POST.get('address1','')+' '+request.POST.get('address2','')
        country=request.POST.get('country','')
        state=request.POST.get('state','')
        zip=request.POST.get('zip','')
        products=request.POST.get('products','')
        comp_pack=Order(name=name,email=email,contact=contact,address=address,country=country,state=state,zip=zip,json_products=products,price=price)
        comp_pack.save()
        order_id=comp_pack.order_id
        updated=Update(order_id=order_id,order_status='Your Order has been placed successfully')
        updated.save()
        thanks=True
        print(products)
        return render(request,'shop/checkout.html',{'thanks':thanks,'id':order_id})
    return render(request,'shop/checkout.html')
def cart(request):
    return HttpResponse('Hello from cart')