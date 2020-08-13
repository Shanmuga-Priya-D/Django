
from django.core import mail

from .models import Contact,Fun,Bookings,BusInfo

from django.http import JsonResponse
import json


from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.mail import EmailMessage

from django.urls import reverse
from .utils import generate_token
from django.views.generic import View

from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib import messages


def home(request):
    return render(request,'home.html')

def contact(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        from_email=settings.EMAIL_HOST_USER
        
            
        
        connection=mail.get_connection()


        connection.open()
        email1=mail.EmailMessage(fname,f'firstname:{fname}\nlastname: {lname} \n email: {email}  \n Query : {message}',from_email,['priyadharmaraj287@gmail.com'],connection=connection)
        connection.send_messages([email1])
        connection.close()
       
        connection.open()
        email2=mail.EmailMessage(f'Hello {fname}','Your Response has been recorded we will get back to you soon ASAP',from_email,[email],connection=connection)
        connection.send_messages([email2])
        connection.close()

        myusercontact=Contact(fname=fname,lname=lname,email=email,subject=subject,message=message)
        myusercontact.save()
       
        return redirect('/')
# https://myaccount.google.com/lesssecureapps please enable less secure app in ur laptop

    return render(request,'contact.html')




def handlesignup(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        passw=request.POST['pass']
        
        
        try:
            if User.objects.get(username=name):
                messages.info(request,"username is already taken")
                return redirect('/')

        except Exception as identifier:
            pass        
        luser=Fun(name=name,email=email)
        luser.save()
        user=User.objects.create_user(name,email,passw)
        user.is_active=False
        user.save()


        current_site=get_current_site(request)
        email_subject='Activate your Roadtravellers account'
        message=render_to_string('activate.html',{
            'user':user,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)

        })
        email_message = EmailMessage(
        email_subject,
        message,
        settings.EMAIL_HOST_USER,
        [email]
 )      
        email_message.send()

        messages.info(request,'We have sent you an email, please confirm your email address to complete registration')
        return redirect('/')

         


def search(request):
    if not request.user.is_authenticated:
        messages.info(request,'Login and Try Again')
        return redirect("/")
    if request.method=='POST':
        fro=request.POST['from']
        to=request.POST['to']
        dat=request.POST['date']
        
        
        buses=BusInfo.objects.all()
        for bus in buses:
            print(bus.id)
        check=Fun.objects.filter(name=request.user)
        
        if len(check)>0:
                entries=Fun.objects.get(name=request.user)
                return render(request,'book.html',{'name':entries,'fro':fro,'to':to,'date':dat,'buses':buses})
               
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('/') 
            
            
    check=Fun.objects.filter(name=request.user)
    if len(check)>0:  
        entries=Fun.objects.get(name=request.user)
        return render(request,'search.html',{'name':entries})
    else:
        messages.info(request,"Invalid Credentials")
        return redirect('/') 
    return render(request,'search.html')

def book(request):
    if not request.user.is_authenticated:
        messages.info(request,'Login and Try Again')
        return redirect("/")
    if request.method=='POST':
        df=Fun.objects.get(name=request.user)
        

        
        return render(request,'confirm.html',{'name':df})
        # return redirect('/update_item')
    return render(request,'book.html')


def confirm(request):
    if not request.user.is_authenticated:
        messages.info(request,'Login and Try Again')
        return redirect("/")
    return render(request,'confirm.html')




def myprofile(request):
    if not request.user.is_authenticated:
        messages.info(request,'Login and Try Again')
        return redirect("/")
   
    
    check=Fun.objects.filter(name=request.user)
    if len(check)>0:
        name=Fun.objects.get(name=request.user)
        print('oooooooooooo')
        print(request.user)
        print('oooooooooooo')
        return render(request,'myprofile.html',{'name':name})
        
    else:
        messages.info(request,"Invalid Credentials")
        return redirect('/')    
    return render(request,'myprofile.html')




def mybookings(request):
    
    
    check=Fun.objects.filter(name=request.user)
    
    if len(check)>0:
        name=Fun.objects.get(name=request.user)        
        books=Bookings.objects.all()
        return render(request,'mybookings.html',{'books':books,'name':name})         
                    
    return render(request,'mybookings.html')
    

def handlelogout(request):
    logout(request)
    return redirect('/')

class LoginView(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        
        email = request.POST.get('email')
        passw = request.POST.get('pass')
        
        user = authenticate(username=email, password=passw)

        if user is not None:
            login(request,user)
            return redirect("/search")
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,'home.html')         


class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_text(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None

        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"Your Account is verified.. Login  now and book your tickets ")
            return redirect('/')
        return render(request,'activate_failed.html',status=402)



def updateItem(request):
    data=json.loads(request.body)
    busid=data['busid']
    action=data['action']
    fro=data['fro']
    to=data['to']
    dat=data['dat']
    
    print(busid)
    print(fro)
    print(to)
    print(dat)
    print(busid)
    m=int(busid)
    buses=BusInfo.objects.all()
    for bus in buses:
        if bus.id==m:
            a=Fun.objects.get(name=request.user)
            mybook=Bookings(user=a,fro=fro,to=to,bus=bus,dat=dat)
            mybook.save()
            print(bus.av_seats)
            bus.av_seats=bus.av_seats-1
            bus.save()
            print(bus.av_seats)

            
            
        
        
        

        
    print('kokokokokokoooooooo')
           
    # return render(request,'confirm.html',{'name':a})
    return HttpResponse('ooio')
    # return JsonResponse('Item was added',safe=False)
