from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from theme.models import Contact
from datetime import datetime

# Create your views here.

context= {
        'var':'Join',
        'link':'login'
    }

context2= {
    'var':'Profile',
    'link':'profile'
}

def signin(request):
    if request.method == "POST":
        n= request.POST.get("name")
        p= request.POST.get("password")

        user = authenticate(username=n, password=p)
        if user is not None:
            #login
            login(request, user)
            var='Profile'
            link='about'
            return render(request, 'index.html', context2)
        else:
           return HttpResponse("bad CREDEDNTIALS")
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        n= request.POST.get("name")
        m= request.POST.get("mobile")
        e= request.POST.get("email")
        p= request.POST.get("password")

        user= User.objects.create_user(username=n, email=e, password=p)
        user.save()

    return render(request, 'signup.html')

def signout(request):
    
    logout(request)
    return render(request, 'index.html', context)


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', context2)
    else:
        return render(request, 'index.html', context)
    
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', context2)
    else:
        return render(request, 'profile.html', context)
        

def about(request):
    if request.user.is_authenticated:
        return render(request, 'about.html', context2)
    else:
        return render(request, 'about.html', context)

def resources(request):
    if request.user.is_authenticated:
        return render(request, 'resources.html', context2)
    else:
        return render(request, 'resources.html', context)

def courses(request):
    if request.user.is_authenticated:
        return render(request, 'courses.html', context2)
    else:
        return render(request, 'courses.html', context)
    
def course1(request):
    if request.user.is_authenticated:
        return render(request, 'course1.html', context2)
    else:
        return render(request, 'course1.html', context)
    
def course2(request):
    if request.user.is_authenticated:
        return render(request, 'course2.html', context2)
    else:
        return render(request, 'course2.html', context)
    
def course3(request):
    if request.user.is_authenticated:
        return render(request, 'course3.html', context2)
    else:
        return render(request, 'course3.html', context)
    
def course4(request):
    if request.user.is_authenticated:
        return render(request, 'course4.html', context2)
    else:
        return render(request, 'course4.html', context)

def course5(request):
    if request.user.is_authenticated:
        return render(request, 'course5.html', context2)
    else:
        return render(request, 'course5.html', context)
    
def course6(request):
    if request.user.is_authenticated:
        return render(request, 'course6.html', context2)
    else:
        return render(request, 'course6.html', context)
    
def course7(request):
    if request.user.is_authenticated:
        return render(request, 'course7.html', context2)
    else:
        return render(request, 'course7.html', context)
    
def course8(request):
    if request.user.is_authenticated:
        return render(request, 'course8.html', context2)
    else:
        return render(request, 'course8.html', context)
    
def event1(request):
    if request.user.is_authenticated:
        return render(request, 'event1.html', context2)
    else:
        return render(request, 'event1.html', context)
    
def event2(request):
    if request.user.is_authenticated:
        return render(request, 'event2.html', context2)
    else:
        return render(request, 'event2.html', context)
    
def event3(request):
    if request.user.is_authenticated:
        return render(request, 'event3.html', context2)
    else:
        return render(request, 'event3.html', context)
    
def event4(request):
    if request.user.is_authenticated:
        return render(request, 'event4.html', context2)
    else:
        return render(request, 'event4.html', context)
    



def thanks(request):
    if request.user.is_authenticated:
        return render(request, 'thanks.html', context2)
    else:
        return render(request, 'thanks.html', context)

def contact(request):
    



    if request.user.is_authenticated:
        if request.method == "POST":
          n= request.POST.get("name")
          e= request.POST.get("email")
          m= request.POST.get("message")

          obj= Contact(name=n, email=e, message=m, date=datetime.today())
          obj.save()
          return render(request, 'thanks.html', context2)
        return render(request, 'contact.html', context2)
    else:
        if request.method == "POST":
          n= request.POST.get("name")
          e= request.POST.get("email")
          m= request.POST.get("message")

          obj= Contact(name=n, email=e, message=m, date=datetime.today())
          obj.save()
          return render(request, 'thanks.html', context)
        return render(request, 'contact.html', context)