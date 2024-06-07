from django.shortcuts import render,redirect
from backend.models import addcategoryDb,productDb
from webapp.models import contactDb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages

def admin_pg(request):
    return render(request,"admin.html")
def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('l1')
        pwd=request.POST.get('l2')
        if User.objects.filter(username__contains=un).exists():
            x= authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request,"Welcome")
                return redirect(index_pg)
            else:
                messages.warning(request,"Invalid User or Password")
                return redirect(admin_pg)
        else:
            messages.warning(request,"User not found")
            return redirect(admin_pg)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_pg)
def index_pg(request):
    return render(request,"index.html")
def add_category_pg(request):
    return render(request,"add_category.html")
def save_ac(request):
    if request.method=="POST":
        a=request.POST.get('a1')
        b=request.POST.get('a2')
        c=request.FILES['a3']
        obj=addcategoryDb(ac_name=a,ac_description=b,ac_image=c)
        obj.save()
        messages.success(request,"Category added successfully")
        return redirect(add_category_pg)
def display_pg(request):
    data=addcategoryDb.objects.all()
    return render(request,"ac_display.html", {'Ddata':data})
def edit_pg(request,Eid):
    data=addcategoryDb.objects.get(id=Eid)
    return render(request,"ac_edit.html",{'Edata':data})
def update_ac(request,Uid):
    if request.method == "POST":
        a = request.POST.get('a1')
        b = request.POST.get('a2')
        try:
            c = request.FILES['a3']
            c_c= FileSystemStorage().save(c.name,c)
        except MultiValueDictKeyError:
            c_c=addcategoryDb.objects.get(id=Uid).ac_image
        addcategoryDb.objects.filter(id=Uid).update(ac_name=a,ac_description=b,ac_image=c_c)
        messages.warning(request, "Updated successfully..!")
        return redirect(display_pg)
def delete_ac(request,Did):
    addcategoryDb.objects.filter(id=Did).delete()
    messages.error(request,"Deleted...")
    return redirect(display_pg)

def product_pg(request):
    cat=addcategoryDb.objects.all()
    return render(request,"product.html",{'cat':cat})
def save_product(request):
    if request.method=="POST":
        a=request.POST.get('b1')
        b=request.POST.get('b2')
        c=request.POST.get('b3')
        d=request.POST.get('b4')
        e=request.FILES['b5']
        obj=productDb(p_category=a,p_name=b,p_price=c,p_description=d,p_image=e)
        obj.save()
        messages.success(request, "Product added successfully")
        return redirect(product_pg)
def P_display_pg(request):
    data=productDb.objects.all()
    return render(request,"prd_display.html", {'DPdata':data})
def P_edit_pg(request,EPid):
    data=productDb.objects.get(id=EPid)
    cat=addcategoryDb.objects.all()
    return render(request,"prd_edit.html",{'EPdata':data,'acEdata':cat})
def P_update(request,UPid):
    if request.method=="POST":
        a=request.POST.get('b1')
        b=request.POST.get('b2')
        c=request.POST.get('b3')
        d=request.POST.get('b4')
        try:
            e = request.FILES['b5']
            e_e=FileSystemStorage().save(e.name,e)
        except MultiValueDictKeyError:
            e_e=productDb.objects.get(id=UPid).p_image
        productDb.objects.filter(id=UPid).update(p_category=a,p_name=b,p_price=c,p_description=d,p_image=e_e)
        messages.warning(request, "Updated successfully..!")
        return redirect(P_display_pg)
def P_delete(request,DPid):
    productDb.objects.filter(id=DPid).delete()
    messages.error(request, "Deleted...")
    return redirect(P_display_pg)


def contact_display_wa(request):
    condata=contactDb.objects.all()
    return render(request,"contact_data.html",{'contactdata':condata})
def delete_contact(request,DCtid):
    contactDb.objects.filter(id=DCtid).delete()
    return redirect(contact_display_wa)
