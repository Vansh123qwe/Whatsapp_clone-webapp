from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Contact
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,login as aj_login,logout
from django.contrib import messages
from . models import frd
from . models import massage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    if request.method=="POST":
        name=request.POST['name']
        content =request.POST['content']
        if len(name)<2 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")

    we=frd.objects.filter(who=request.user)
    '''frdd={}
    for g in qwe:
        if g.who == request.user:
            frdd[fr]= g.friend'''
    
    return render(request, 'home/home.html', {'frdd':we})

def about(request):
    products= Contact.objects.all()
    param={'product':products}
    return render(request, 'home/about.html',param)    

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

            # check for errorneous input
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('login')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('login')

        if (pass1!= pass2):
            messages.error(request, " Passwords do not match")
            return redirect('login')

            # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('login')

    else:
        return HttpResponse("404 - Not found")

def handlelogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['username']
        loginpassword=request.POST['password']
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            aj_login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("login")

    return HttpResponse("404- Not found")

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("login")


def users(request):
    query=request.POST['query']
    ee=User.objects.filter(username__icontains=query)
    par={'pro':ee}
    return render(request, 'home/user.html',par)  

def add(request):
    if request.method=="POST":
        cnt=0
        for h in request.POST:
            if(cnt>0):
                un=h
            cnt+=1
        #print(ww,"ooooooook")
        #print(request.POST,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        #un=request.POST["{{i}}"]
        asd=frd(friend=un, who= request.user)
        aq=frd(who=un, friend=request.user)
        asd.save()
        aq.save()
        return redirect("home")

@csrf_exempt
def nam(request, name):
    fg=name
    nam.poi=fg
    if request.method=="POST":
        a=massage.objects.filter(who=request.user, whom= name)
        b=massage.objects.filter(whom=request.user, who= name)
        c=(a | b).distinct()
       # print(c[0].body,request.user, name)
        c=c.order_by('timeStamp')
        mas={}
        cn=0
        for h in c:
            w={}
            w['body']=h.body
            w['time']=h.timeStamp
            w['who']=h.who
            w['whom']=h.whom
            mas[cn]=w
            cn+=1
        return JsonResponse(mas)
     #   return redirect("home")

def send(request):
    if request.method=="POST":
        msg= request.POST['naa']
        '''msg=request.POST['send']'''
        
        wh=nam.poi
        zx=massage(who=request.user, whom=wh, body=msg)
        zx.save()
        return HttpResponse('')



