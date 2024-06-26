import razorpay
from django.shortcuts import render, redirect
from backend.models import productDb, addcategoryDb
from webapp.models import contactDb, Reg_signUp, cartDb,checkoutDb
from django.contrib import messages


def home_pg(request):
    cdata = addcategoryDb.objects.all()
    return render(request, "home.html", {'catdata': cdata})


def about_pg(request):
    cdata = addcategoryDb.objects.all()
    return render(request, "about.html", {'catdata': cdata})


def contact_pg(request):
    cdata = addcategoryDb.objects.all()
    return render(request, "contact.html", {'catdata': cdata})


def save_contact(request):
    if request.method == "POST":
        a = request.POST.get('c1')
        b = request.POST.get('c2')
        c = request.POST.get('c3')
        d = request.POST.get('c4')
        e = request.POST.get('c5')
        obj = contactDb(contact_name=a, contact_email=b, contact_number=c, contact_subject=d, contact_message=e)
        obj.save()
        return redirect(contact_pg)


def shope_pg(request):
    pdata = productDb.objects.all()
    cdata = addcategoryDb.objects.all()
    return render(request, "shope.html", {'prodata': pdata, 'catdata': cdata})


def filtered_products_pg(request, P_catname_id):
    P_catnamedata = productDb.objects.filter(p_category=P_catname_id)
    s = addcategoryDb.objects.filter(ac_name=P_catname_id)
    cdata = addcategoryDb.objects.all()
    return render(request, "product_filtered.html", {'P_catnamedata': P_catnamedata, 's': s, 'catdata': cdata})


def single_product_pg(request, Pid):
    pdata = productDb.objects.get(id=Pid)
    cdata = addcategoryDb.objects.all()
    return render(request, "single_product.html", {'ppdata': pdata, 'catdata': cdata})


def registration_pg(request):
    return render(request, "registration.html")


def save_registration_signUp(request):
    if request.method == "POST":
        a = request.POST.get('e1')
        b = request.POST.get('e2')
        c = request.POST.get('e3')
        d = request.POST.get('e4')
        e = request.FILES['e5']
        obj = Reg_signUp(su_username=a, su_password=b, su_conformpassword=c, su_email=d, su_pic=e)
        if Reg_signUp.objects.filter(su_username=a).exists():
            messages.warning(request, "User already exists..")
        elif Reg_signUp.objects.filter(su_email=d).exists():
            messages.warning(request, "Email already exists..")
        else:
            messages.success(request, "login successfull..")
            obj.save()
        return redirect(registration_pg)


def UserLogin_su(request):
    if request.method == "POST":
        su_un = request.POST.get('d1')
        su_pwd = request.POST.get('d2')
        if Reg_signUp.objects.filter(su_username=su_un, su_password=su_pwd).exists():
            request.session['su_username'] = su_un
            request.session['su_password'] = su_pwd
            messages.success(request, "Login Successfully")
            return redirect(home_pg)
        else:
            messages.warning(request, "Invalid User")
            return redirect(registration_pg)
    else:
        messages.warning(request, "Undefined User")
        return redirect(registration_pg)


def UserLogout_su(request):
    del request.session['su_username']
    del request.session['su_password']
    return redirect(registration_pg)


def save_cart(request):
    if request.method == "POST":
        a = request.POST.get('a4')
        b = request.POST.get('a5')
        c = request.POST.get('a1')
        d = request.POST.get('a3')
        obj = cartDb(cart_username=a, cart_productname=b, cart_quantity=c, cart_price=d)
        obj.save()
        messages.success(request, "Added to Cart")
        return redirect(home_pg)


def cart_pg(request):
    cartdata = cartDb.objects.filter(cart_username=request.session['su_username'])
    cdata = addcategoryDb.objects.all()

    total_price = 0
    shipping_fee = 0
    total_shipping_Overall = 0
    for i in cartdata:
        total_price = total_price + i.cart_price
        if total_price < 100:
            shipping_fee = 100
        else:
            shipping_fee = 0
        total_shipping_Overall = total_price + shipping_fee

    return render(request, "cart.html",
                  {'cartdata': cartdata, 'catdata': cdata, 'total_price': total_price, 'shipping_fee': shipping_fee,
                   'total_shipping_Overall': total_shipping_Overall})


def delete_cartitem(request, Dcid):
    cartDb.objects.get(id=Dcid).delete()
    return redirect(cart_pg)


def checkout_Pg(request):
    cdata = addcategoryDb.objects.all()
    # cartdataUsername will display the product based on the userlogin since we have used the filter session method
    cartdataUsername = cartDb.objects.filter(cart_username=request.session['su_username'])
    subTotal = 0
    shippingPrice = 0
    overAllTotal = 0
    for i in cartdataUsername:
        subTotal = subTotal + i.cart_price
        if subTotal < 100:
            shippingPrice = 100
        else:
            shippingPrice = 0
        overAllTotal = subTotal + shippingPrice
        messages.success(request,"Redirected to Payment page")
    return render(request, "checkout.html",
                  {'catdata': cdata, 'cartdataUsername': cartdataUsername, 'subTotal': subTotal,
                   'shippingPrice': shippingPrice, 'overAllTotal': overAllTotal})
def payment_pg(request):
    customer=checkoutDb.objects.order_by('-id').first()

    # get the amount of the current customer
    pay =customer.checkout_overall_total

    #
    amount = int(pay*100)

    #
    pay_str = str(amount)

    for i in pay_str:
        print(i)
    if request.method =="POST":
        order_currency ='INR'
        client = razorpay.Client(auth=('rzp_test_7apnMZ22irzosy','mlTDHZRjKcZpIfDGoQVKW6WQ'))
        payment=client.order.create({'amount':amount, 'order_currency':order_currency,'payment_capture':'1'})

    return render(request,"payment.html",{'customer':customer,'pay_str':pay_str})
def save_checkout(request):
    if request.method=="POST":
        co_username= request.POST.get('cartproname')
        co_email= request.POST.get('cartproemail')
        co_place= request.POST.get('cartproplace')
        co_address= request.POST.get('cartproaddress')
        co_phone= request.POST.get('cartpronumber')
        co_message= request.POST.get('cartpromessage')
        co_totalprice= request.POST.get('cartprototal')
        obj=checkoutDb(checkout_username=co_username,checkout_email=co_email,checkout_place=co_place,checkout_address=co_address,checkout_Phone=co_phone,checkout_message=co_message,checkout_overall_total=co_totalprice)
        obj.save()
        return redirect(payment_pg)
