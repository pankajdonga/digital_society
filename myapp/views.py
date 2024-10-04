from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail  
from .forms import *
from .models import *
from chairman.models import *
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import random
from digitalSocity import settings
# Create your views here.
@login_required
def index(request):
    uid=request.session.get('uid')
    cid=CustomUser.objects.get(id=uid)
    data=invoice.objects.all().filter(email=cid)
    event=AddEvent.objects.all()
    return render(request,'socmember/index.html',{'user':cid,'data':data,'event':event})

def userlogin(request):
    if request.method=='POST':
        mail=request.POST['email']
        pas=request.POST['password']
        username=CustomUser.objects.get(email=mail)
        user=authenticate(request, email=mail, password=pas)
        if user is not None and user.is_active and not user.is_superuser:
            login(request, user)
            request.session['username']=mail
            request.session['uid']=username.id
            return redirect('index')
        elif user is not None and user.is_superuser:
            login(request, user)
            request.session['uid']=username.id
            return redirect('adminindex')
        else:
            print('Error....')
    return render(request,'socmember/userlogin.html')

def user_logout(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method=='POST':
        new=CustomUserForm(request.POST,request.FILES)
        if new.is_valid():
            user=new.save()
            login(request,user)
            print('Signup Successfully...')

            #login code
            global otp
            otp=random.randint(11111,99999)
            name=request.POST['first_name']
            sub='Your OTP Verification Code'
            mes=f'Dear {name}\n\nThank you for signing up with us. To verify your email, please enter the following\n\nOne Time Password (OTP): {otp}\n\nBest regards,\n\nGokuldham Society'
            send_to=settings.EMAIL_HOST_USER
            to_id=[request.POST['email']]
            send_mail(subject=sub,message=mes,from_email=send_to,recipient_list=to_id)
            return redirect('verifyotp')
        else:
            print(new.errors)
    return render(request,'socmember/signup.html')

def verifyotp(request):
    global otp
    print('otp', otp)
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            print("Verification Successfull!")
            return redirect('/')
        else:
            print('Please Enter Valid Otp.')
    return render(request,'socmember/verifyotp.html')

def invoiceReport(request,id):
    uid=request.session.get('uid')
    cid=CustomUser.objects.get(id=uid)
    data=invoice.objects.get(id=id)
    request.session['data']=id
    logo=SocietyLogo.objects.all()
    return render(request,'socmember/invoiceReport.html',{'user':cid,'data':data,'logo':logo})

def notice(request):
    uid=request.session.get('uid')
    cid=CustomUser.objects.get(id=uid)
    data=invoice.objects.all().filter(email=cid)
    return render(request,'socmember/notice.html',{'user':cid,'data':data})

def event(request):
    uid=request.session.get('uid')
    cid=CustomUser.objects.get(id=uid)
    data=AddEvent.objects.all()
    return render(request,'socmember/event.html',{'user':cid,'data':data})

def societymember(request):
    uid=request.session.get('uid')
    cid=CustomUser.objects.get(id=uid)
    data=CustomUser.objects.all().filter(is_active=True, is_staff=False, is_superuser=False)
    return render(request,'socmember/societymember.html',{'user':cid,'data':data})

def watchman(request):
    uid=request.session.get('uid')
    cid=CustomUser.objects.get(id=uid)
    watchmandata=CustomUser.objects.all().filter(is_active=True, is_staff=True, is_superuser=False)
    return render(request,'socmember/watchman.html',{'user':cid,'watchmandata':watchmandata})

def profile(request):
    uid=request.session.get('uid')
    cid=CustomUser.objects.get(id=uid)
    if request.method=='POST':
        form=CustomUserUpdateForm(request.POST,request.FILES,instance=cid)
        if form.is_valid():
            form.save()
            print('Data updated...')
            return redirect('index')
        else:
            print(form.errors)
    return render(request,'socmember/profile.html',{'user':cid})

def pdf(request):
    uid=request.session.get('uid')
    cid=CustomUser.objects.get(id=uid)
    invid=request.session.get('data')
    logo=SocietyLogo.objects.all()
    data=invoice.objects.get(id=invid)

    template_path = 'socmember/pdf.html'

    context={'user':cid,'data':data,'logo':logo}
    
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="invoice.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

    
