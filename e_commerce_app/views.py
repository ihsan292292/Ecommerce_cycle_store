from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib.auth import logout
from django.contrib import messages
import datetime
from datetime import timedelta
import re
from django.core.mail import send_mail
from e_commerce.settings import EMAIL_HOST_USER

# Create your views here.
def index(request):
    c = add_product.objects.all()
    bt= []
    ar= []
    brnd = []
    spd = []
    colr = []
    pr = []
    file_im = []
    ids=[]
    for i in c:
        bike_id=i.id
        ids.append(bike_id)
        bike_type=i.bike_type
        bt.append(bike_type)
        age_range = i.age_range
        ar.append(age_range)
        brand = i.brand
        brnd.append(brand)
        noOfSpeed=i.noOfSpeed
        spd.append(noOfSpeed)
        color = i.color
        colr.append(color)
        price=i.price
        pr.append(price)
        image1=str(i.file_image).split('/')[-1]
        file_im.append(image1)
    mylist=zip(ids,bt,ar,brnd,spd,colr,pr,file_im)
    print(mylist)
    return render(request,'index.html',{'data':mylist})

def seller_log(request):
    a = seller_register.objects.all()
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        for i in a:
            if(i.email == email and i.password== password):
                request.session['s_id']=i.id #global
                return redirect(seller_profile)
        else:
            return HttpResponse("login failed!")
    return render(request,'login.html')

def seller_reg(request):
    if request.method=='POST':
        name = request.POST.get('seller_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profile = request.FILES.get('profile_image')
        company_name = request.POST.get('company_name')
        company_details = request.POST.get('company_details')
        password = request.POST.get('password')
        cpassword =request.POST.get('cpassword')
        if password==cpassword:
            a=seller_register(seller_name=name,email=email,company_name=company_name,phone=phone,company_details=company_details,password=password,photo=profile)
            a.save()
            return redirect(seller_log)
    return render(request,'seller-reg.html')

def prod_add(request):
    if request.method=='POST':
        bike_type = request.POST.get('bike_type')
        age_range = request.POST.get('age_range')
        brand = request.POST.get('brand')
        noOfSpeed = request.POST.get('speed')
        color = request.POST.get('color')
        price = request.POST.get('price')
        file_image = request.FILES.get('file_image')
        a=add_product(bike_type=bike_type,age_range=age_range,brand=brand,noOfSpeed=noOfSpeed,color=color,price=price,file_image=file_image)
        a.save()
        return redirect(view_cycle_seller)
    return render(request,'product-add.html')

def seller_profile(request):
    id1 = request.session['s_id']
    a = seller_register.objects.get(id=id1)
    img = str(a.photo).split('/')[-1]
    return render(request,'profile.html',{'data':a,'img':img})

def edit_seller_profile(request):
    id1 = request.session['s_id']
    a = seller_register.objects.get(id=id1)
    img = str(a.photo).split('/')[-1]
    if request.method=='POST':
        a.seller_name = request.POST.get('seller_name')
        a.email = request.POST.get('email')
        a.phone = request.POST.get('phone')
        a.company_name = request.POST.get('company_name')
        a.company_details = request.POST.get('company_details')
        if request.FILES.get('profile_image')==None:
            a.save()
        else:
            a.photo = request.FILES.get('profile_image')
            a.save()    
        return redirect(seller_profile)
    return render(request,'edit-profile.html',{'data':a,'img':img})

def view_cycle_seller(request):
    id1 = request.session['s_id']
    b = seller_register.objects.get(id=id1)
    a = add_product.objects.all()
    bt= []
    ar= []
    brnd = []
    spd = []
    colr = []
    pr = []
    file_im = []
    ids=[]
    for i in a:
        bike_type=i.bike_type
        bt.append(bike_type)
        bike_id=i.id
        ids.append(bike_id)
        age_range = i.age_range
        ar.append(age_range)
        brand = i.brand
        brnd.append(brand)
        noOfSpeed=i.noOfSpeed
        spd.append(noOfSpeed)
        color = i.color
        colr.append(color)
        price=i.price
        pr.append(price)
        image1=str(i.file_image).split('/')[-1]
        file_im.append(image1)
    mylist=zip(bt,ar,brnd,spd,colr,pr,file_im, ids)
    return render(request,'view-product-seller.html',{'data':mylist,'b':b})

def edit_cycle(request, id):
    b = add_product.objects.get(id=id)
    img = str(b.file_image).split('/')[-1]
    if request.method=='POST':
        b.bike_type = request.POST.get('bike_type')
        b.age_range = request.POST.get('age_range')
        b.brand = request.POST.get('brand')
        b.noOfSpeed = request.POST.get('speed')
        b.color = request.POST.get('color')
        b.price = request.POST.get('price')
        if request.FILES.get('file_image')==None:
            b.save()
        else:
            b.file_image = request.FILES.get('file_image')
            b.save()    
        return redirect(view_cycle_seller)
    return render(request,'edit-cycle.html',{'data':b,'img':img})

def delete_cycle(request,id):
    b = add_product.objects.get(id=id)
    b.delete()
    return redirect(view_cycle_seller)

def seller_logout(request):
    logout(request)
    return redirect(index)

# ...........................................................

def buy_reg(request):
    if request.method=='POST':
        name = request.POST.get('seller_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        password = request.POST.get('password')
        cpassword =request.POST.get('cpassword')
        a=buyer_register.objects.all()
        model_name = []
        model_email = []
        for i in a:
            model_email.append(i.email)
            model_name.append(i.name)
        if password==cpassword:
            if name in model_name:
                return HttpResponse("Username is already exist!!")
            if email in model_email:
                return HttpResponse("Password is already exist!!")
            a=buyer_register(name=name,email=email,phone=phone,password=password,street=street,city=city,state=state,pincode=pincode)
            a.save()
            return HttpResponse("Registration sucessfully!!")
    return render(request,'buyer-reg.html')

def buyer_log(request):
    a = buyer_register.objects.all()
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        for i in a:
            if(i.email == email and i.password == password):
                request.session['us_id']=i.id #global
                return redirect(buyer_index_all)
        else:
            return HttpResponse("login failed!")
    return render(request,'buyer-log.html')

def buyer_index_all(request):
    id2 = request.session['us_id']
    a = buyer_register.objects.get(id=id2)
    c = add_product.objects.all()
    bt= []
    ar= []
    brnd = []
    spd = []
    colr = []
    pr = []
    file_im = []
    ids=[]
    for i in c:
        bike_id=i.id
        ids.append(bike_id)
        bike_type=i.bike_type
        bt.append(bike_type)
        age_range = i.age_range
        ar.append(age_range)
        brand = i.brand
        brnd.append(brand)
        noOfSpeed=i.noOfSpeed
        spd.append(noOfSpeed)
        color = i.color
        colr.append(color)
        price=i.price
        pr.append(price)
        image1=str(i.file_image).split('/')[-1]
        file_im.append(image1)
    mylist=zip(ids,bt,ar,brnd,spd,colr,pr,file_im)
    return render(request,'buyer-index-all.html',{'data':mylist,'name':a})

def buyer_index_b_type(request,url_variable):
    id2 = request.session['us_id']
    a = buyer_register.objects.get(id=id2)
    c = add_product.objects.all()
    bt= []
    ar= []
    brnd = []
    spd = []
    colr = []
    pr = []
    file_im = []
    ids=[]
    for i in c:
        bike_id=i.id
        ids.append(bike_id)
        bike_type=i.bike_type
        bt.append(bike_type)
        age_range = i.age_range
        ar.append(age_range)
        brand = i.brand
        brnd.append(brand)
        noOfSpeed=i.noOfSpeed
        spd.append(noOfSpeed)
        color = i.color
        colr.append(color)
        price=i.price
        pr.append(price)
        image1=str(i.file_image).split('/')[-1]
        file_im.append(image1)
    mylist=zip(ids,bt,ar,brnd,spd,colr,pr,file_im)
    
    
    url_variable = url_variable.replace('_',' ')
    
    return render(request,'buyer-index.html',{'name':a,'data':mylist,'url_variable':url_variable})

def buyer_profile(request):
    try:
        id1 = request.session['us_id']
        a = buyer_register.objects.get(id=id1)
        if request.method == 'POST':
            a.name = request.POST.get('fullName')
            a.email = request.POST.get('eMail')
            a.phone = request.POST.get('phone')
            a.password = request.POST.get('password')
            a.street = request.POST.get('Street')
            a.city = request.POST.get('ciTy')
            a.state = request.POST.get('sTate')
            a.pincode = request.POST.get('pIn')
            a.save()
            return redirect(buyer_index_all)
    except:
        request.session['us_id'] = None
        return redirect(buyer_log)
        
    return render(request,'buyer-profile.html',{'data':a})

def buyer_logout(request):
    logout(request)
    return redirect(index)

def add_wishlist(request,id):
    id1 = request.session['us_id']
    a = add_product.objects.get(id=id)
    c = wishlist.objects.all()
    for i in c:
        if id == i.prod_id and id1 == i.user_id:
            messages.error(request,"item already exist") 
            break
    else:        
        b = wishlist(user_id=id1,prod_id=a.id,bike_type=a.bike_type,age_range=a.age_range,brand=a.brand,noOfSpeed=a.noOfSpeed,color=a.color,price=a.price,file_image=a.file_image)
        b.save()
        messages.success(request,"Successfully added to wishlist")
    return redirect(buyer_index_all)
    
def view_wishlist(request):
    id3 = request.session['us_id'] # login user id
    c = wishlist.objects.all()
    uid = []
    proid = []
    bt= []
    ar= []
    brnd = []
    spd = []
    colr = []
    pr = []
    file_im = []
    wish_id = []
    for i in c: 
        wish_id.append(i.id)
        prod_id = i.prod_id
        proid.append(prod_id)
        user_id=i.user_id
        uid.append(user_id)
        bike_type=i.bike_type
        bt.append(bike_type)
        age_range = i.age_range
        ar.append(age_range)
        brand = i.brand
        brnd.append(brand)
        noOfSpeed=i.noOfSpeed
        spd.append(noOfSpeed)
        color = i.color
        colr.append(color)
        price=i.price
        pr.append(price)
        image1=str(i.file_image).split('/')[-1]
        file_im.append(image1)
    mylist=zip(uid,proid,bt,ar,brnd,spd,colr,pr,file_im,wish_id)
    print(wish_id)
    print(prod_id)
    return render(request,'wishlist.html',{'data':mylist,"u_id":id3})

def delete_wishlist(request,id):
    
    b = wishlist.objects.get(id=id)
    b.delete()
    return redirect(view_wishlist)

def add_cart(request,id):
    id1 = request.session['us_id']
    a = add_product.objects.get(id=id)
    c = cart.objects.all()
    print(id1)
    for i in c: 
        if id == i.prod_id and id1 == i.user_id:
            i.quantity+=1
            i.price = int(a.price) * i.quantity
            i.save()
            messages.error(request,"item already exist and incremented by one") 
            break
    else:
        count = 1
        b = cart(user_id=id1,prod_id=a.id,quantity=count,bike_type=a.bike_type,age_range=a.age_range,brand=a.brand,noOfSpeed=a.noOfSpeed,color=a.color,price=a.price,file_image=a.file_image)
        b.save()
        messages.success(request,'Successfully added in Cart!!')

    return redirect(buyer_index_all)
        
def view_cart(request):
    id1 = request.session['us_id']
    buyer = buyer_register.objects.get(id=id1)
    c = cart.objects.all()
    uid = []
    proid = []
    count = []
    bt= []
    ar= []
    brnd = []
    spd = []
    colr = []
    pr = []
    file_im = []
    cart_id = []
    for i in c:
        cart_id.append(i.id)
        proid.append(i.prod_id)
        uid.append(i.user_id)
        count.append(i.quantity)
        bt.append(i.bike_type)
        ar.append(i.age_range)
        brnd.append(i.brand)
        spd.append(i.noOfSpeed)
        colr.append(i.color)
        pr.append(i.price)
        image1=str(i.file_image).split('/')[-1]
        file_im.append(image1)
    tp1 = []
    tp2 = []
    # print(uid)
    # print(id1)

    # Total Price
    d = cart.objects.filter(user_id=id1)
    for i in d:
        # print(i.price)
        tp1.append(i.price)
        # print(tp1)
    for i in tp1:
        tp2.append(int(i))
    # print(tp2)
    total_price = sum(tp2)
    
    new_total_price = total_price - 100
    
    request.session['total_price'] = new_total_price 
    
    mylist=zip(uid,proid,count,bt,ar,brnd,spd,colr,pr,file_im,cart_id)
    
    # Add address
    
    if request.method == "POST":
        add = {}
        name = request.POST.get("name")
        street = request.POST.get("street")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address_items = {'name': name, 'street': street, 'city':city, 'state':state, 'pincode':pincode, 'email':email, 'phone':phone}
        add.update(address_items)
        request.session['address'] = add
        print(request.session['address'])
        messages.success(request,"Address Added Successfully")
    return render(request,'cart.html',{'data':mylist,"u_id":id1,'buyer':buyer,"tp":total_price})

def delete_cart(request,id):
    a = cart.objects.get(id=id)
    a.delete()
    return redirect(view_cart)

def increment_cart_pro(request,id):
    a = cart.objects.get(id=id)
    b = add_product.objects.get(id=a.prod_id)
    a.quantity+=1
    print(a.price)
    a.price = a.quantity * int(b.price)
    a.save()
    return redirect(view_cart)

def decrement_cart_pro(request,id):
    a = cart.objects.get(id=id)
    b = add_product.objects.get(id=a.prod_id)
    a.quantity+=-1
    a.price = a.quantity * int(b.price)
    a.save()
    return redirect(view_cart)


def delivery_details_add(request):
    id1 = request.session['us_id']
    total_price = request.session['total_price']
    a = cart.objects.all()
    name = buyer_register.objects.get(id = id1)
    address = request.session['address']
    products = ""
    images = ""
    nowdate = datetime.date.today()
    edate = nowdate+timedelta(days=10)
    for i in a:
        if id1 == i.user_id:
            pro_items = "product_id:"+str(i.prod_id)+"\n quantity:"+str(i.quantity)+"\n bike_type:"+i.bike_type+"\n age_range:"+i.age_range+"\n brand:"+i.brand+"\n no of speed:"+i.noOfSpeed+"\n colour:"+i.color+"\n price:"+i.price+"\n\n\n\n"
            products = products + pro_items
            products_image=str(i.file_image).split('/')[-1]
            images = images+" "+products_image
            pro_brand = i.brand
    b = delivary_details(uname=name.name,address=address,user_id=id1,products=products,estimated_delivery=edate,products_image=images,total_amount_paid=total_price)
    b.save()
    
    c=cart.objects.all()
    c.delete()
    
    print(address)
    
    email_host = EMAIL_HOST_USER
    
    send_mail(
    "Order Success Message",
    f"Your Orders:{pro_brand} Successfully orderd!!",
    email_host,
    ["kathayik771@gmail.com"],
    fail_silently=False,
)
    # print(images)
    # print(products)
    # print(name.name)
    # print(total_price)
     
    return redirect(order_success)
    
def order_success(request):
    id1 = request.session['us_id']
    b = buyer_register.objects.get(id=id1)
    a = delivary_details.objects.filter(user_id=id1)
    c = delivary_details.objects.all()
    # Initialize a list to store bike types
    bike_types = []
    brands = []
    quantities = []
    prices = []
    
    for i in a:
        entries = i.products.split(" ")
        total_price = i.total_amount_paid
        img_list = i.products_image.split()

   
        
    # Parse each entry to find the "bike_type"
    for entry in entries:
        if entry.startswith("bike_type:"):
            # Extract the "bike_type" value and append it to the list
            bike_type = entry.split(":")[1]
            bike_types.append(bike_type)
            
        if entry.startswith("brand:"):
            # Extract the "brand" value and append it to the list
            brand = entry.split(":")[1]
            brands.append(brand)
            
        if entry.startswith("quantity:"):
            # Extract the "quantity" value and append it to the list
            quantity = entry.split(":")[1]
            quantities.append(quantity)
            
        if entry.startswith("price:"):
            # Extract the "price" value and append it to the list
            price = entry.split(":")[1]
            prices.append(price)
            
    price_pattern = r'\d+'  # Matches one or more digits

    # Use a list comprehension to extract prices as integers
    nprices = [int(re.search(price_pattern, item).group()) for item in prices if re.search(price_pattern, item)]

    # Print the list of bike types
    for bike_type in bike_types:
        print("Bike Type:", bike_type)
        
    for brand in brands:
        print("Brand:", brand)
        
    for quantity in quantities:
        print("Quantity:", quantity)
    
    for price in prices:
        print("Price:", price)
    
    print(brands)
    nbrand=[]
    for i in brands:
        nbrand.append(i.strip())
    print(nbrand)
    nquantity=[]
    print(quantities)
    for i in quantities:
        nquantity.append(i.strip())
    print(nquantity)
    print(nprices)
    print(img_list)
    
    mylist = zip(nbrand,bike_types,nquantity,img_list,nprices)

    return render(request,'order-placed.html',{'data':mylist,'name':b,'total_price':total_price})

def view_orderd(request):
    c = delivary_details.objects.all()
    id1 = request.session['us_id']
    b = buyer_register.objects.get(id=id1)
    bike_types = []
    brands = []
    quantities = []
    prices = []
    
    
    for i in c:
        if i.user_id == id1:
            img_list = i.products_image.split()
            entries = i.products.split(" ")
            total_price = i.total_amount_paid
            print(i.products)
        
    
        
    # Parse each entry to find the "bike_type"
    for entry in entries:
        if entry.startswith("bike_type:"):
            # Extract the "bike_type" value and append it to the list
            bike_type = entry.split(":")[1]
            bike_types.append(bike_type)
            
        if entry.startswith("brand:"):
            # Extract the "brand" value and append it to the list
            brand = entry.split(":")[1]
            brands.append(brand)
            
        if entry.startswith("quantity:"):
            # Extract the "quantity" value and append it to the list
            quantity = entry.split(":")[1]
            quantities.append(quantity)
            
        if entry.startswith("price:"):
            # Extract the "price" value and append it to the list
            price = entry.split(":")[1]
            prices.append(price)
            
    price_pattern = r'\d+'  # Matches one or more digits

    # Use a list comprehension to extract prices as integers
    nprices = [int(re.search(price_pattern, item).group()) for item in prices if re.search(price_pattern, item)]


    # Print the list of bike types
    for bike_type in bike_types:
        print("Bike Type:", bike_type)
        
    for brand in brands:
        print("Brand:", brand)
        
    for quantity in quantities:
        print("Quantity:", quantity)
    
    for price in prices:
        print("Price:", price)
    
    print(brands)
    nbrand=[]
    for i in brands:
        nbrand.append(i.strip())
    print(nbrand)
    nquantity=[]
    print(quantities)
    for i in quantities:
        nquantity.append(i.strip())
    print(nquantity)
    print(nprices)
    print(img_list)
    print(total_price)
    
    mylist = zip(nbrand,bike_types,nquantity,img_list,nprices)
    
    print(mylist)  
    return render(request,'view_total_orders.html',{'data':mylist,'total_price':total_price,'orders':c})
    
    


