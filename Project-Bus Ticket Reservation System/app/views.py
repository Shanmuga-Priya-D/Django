from django.shortcuts import render,HttpResponse,redirect
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



# Create your views here.

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

def signup(request):
    if request.method == 'POST':
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['pass']
        


        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        
    return redirect('/')






