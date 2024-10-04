from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.shortcuts import render
from myapp.forms import *
from myapp.models import *
from myapp.views import *
from .forms import *
from .models import *

# Create your views here.

def adminindex(request):
    uid=request.session.get('uid')
    cid=CustomUser.objects.get(id=uid)
    invoices=invoice.objects.all()
    event=AddEvent.objects.all()
    return render(request, 'socadmin/adminindex.html',{'user':cid,'invoices':invoices,'event':event})

def adminmember(request):
    uid=request.session.get('uid')
    cid=CustomUser.objects.get(id=uid)
    data=CustomUser.objects.all().filter(is_active=True,is_staff=False,is_superuser=False)
    return render(request,'socadmin/adminmember.html',{'user':cid,'data':data})

def adminwatchman(request):
    uid=request.session.get('uid')
    cid=CustomUser.objects.get(id=uid)
    data=CustomUser.objects.all().filter(is_active=True,is_staff=True,is_superuser=False)
    return render(request, 'socadmin/adminwatchman.html',{'user':cid,'data':data})

def adminnotice(request):
    uid=request.session.get('uid')
    cid=CustomUser.objects.get(id=uid)
    
    data=invoice.objects.all()
    return render(request, 'socadmin/adminnotice.html',{'user':cid,'data':data})

def adminevent(request):
    uid=request.session.get('uid')
    cid=CustomUser.objects.get(id=uid)
    data=AddEvent.objects.all()
    return render(request, 'socadmin/adminevent.html',{'user':cid,'data':data})

def addmember(request):
    if request.method=='POST':
        new=CustomUserForm(request.POST,request.FILES)
        if new.is_valid():
            new.save()
            print('Signup Successfully...')
        else:
            print(new.errors)
    return render(request, 'socadmin/addmember.html')

def deletemember(request,id):
    print(id)
    mid=CustomUser.objects.get(id=id)
    CustomUser.delete(mid)
    return redirect('adminmember')

def adminprofile(request):
    uid=request.session.get('uid')
    cid=CustomUser.objects.get(id=uid)
    return render(request, 'socadmin/adminprofile.html',{'cid':cid})

def adminlogout(request):
    logout(request)
    return redirect('/')


num=000
def createinvoice(request):
    global num
    num += 1
    inv='INV-000' + str(num)
    print(inv)
    data=CustomUser.objects.all().filter(is_active=True,is_staff=False,is_superuser=False)

    if request.method=='POST':
        form=InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            print('data inserted!')
            return redirect('adminnotice')
        else:
            print(form.errors)
    return render(request, 'socadmin/createinvoice.html',{'data':data,'inv':inv})


def addwatchman(request):
    if request.method=='POST':
        new=CustomUserForm(request.POST,request.FILES)
        if new.is_valid():
            new.save()
            print('Signup Successfully...')
            return redirect('adminwatchman')
        else:
            print(new.errors)
    return render(request,'socadmin/addwatchman.html')


def deleteinvoice(request,id):
    invoiceid=invoice.objects.get(id=id)
    invoice.delete(invoiceid)
    return redirect('adminnotice')

def deletewatchman(request,id):
    wid=CustomUser.objects.get(id=id)
    CustomUser.delete(wid)
    return redirect('adminwatchman')

def addevent(request):
    if request.method=='POST':
        form=AddEventForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print('Data Inserted!')
        else:
            print(form.errors)
    return render(request,'socadmin/addevent.html')


def deleteevent(request,id):
    eventid=AddEvent.objects.get(id=id)
    AddEvent.delete(eventid)
    return redirect('adminevent')
