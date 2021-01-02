from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')


def login(request):
    return render (request, 'login.html')

def signup(request):
    if request.method == "POST":
        #SIGN IN HANDLING
        if request.POST['password'] == request.POST['password2']:
            if request.POST['username'] and request.POST['email'] and request.POST['password']:
                try:
                    user = User.objects.get(email= request.POST['email'])
                    return render(request, 'signup.html', { 'error' : "User already exists!"})
                except User.DoesNotExist:
                    User.objects.create_user(
                        username = request.POST['username'],
                        email = request.POST['email'],
                        password = request.POST['password']
                    )
                    messages.success(request, "Signup Successful, <br> Login Here")
                    return redirect(login)
            else:
                return render(request, 'signup.html', { 'error' : "Insert the Required Fields"})
        else:
            return render(request, 'signup.html', { 'error' : "Passwords Don't Match"})
        
    
    else:
        return render(request, 'signup.html')




# def login(request):
#     return render (request, 'login.html')
