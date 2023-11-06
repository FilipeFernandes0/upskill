from django.shortcuts import render,redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.contrib import auth

# email validation. 
# To check whether the email provided is valid and 
# not already in use.

class EmailValidationView(View):
    def post(self,request):
        data = json.loads(request.body)
        email = data['email']

        if not validate_email(email):
            return JsonResponse({'email_error':'Email is invalid'},status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'sorry this email is in use chosse another one'},status=400)
        return JsonResponse({'email_valid':True})

#username validation. 
# To check whether the username 
# provided contains only alphanumeric characters 
# and is not already in use.


class UsernameValidationView(View):
    def post(self,request):
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error':'username should only contain alphanumeric characters'},status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'sorry username in use, choose another one'},status=400)
        return JsonResponse({'username_valid':True})

# user registration process. 
# to checks if the provided username and email are not already in use
# and if the password is of sufficient length.

class RegistrationView(View):
    def get(self,request):
        return render(request, 'authentication/register.html')
    
    def post(self,request):
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():

                    if len(password)<6:
                        messages.error(request,"Password too short")
                        return render(request, 'authentication/register.html', context)
                    user =  User.objects.create_user(username=username,email=email)
                    user.set_password(password)
                    user.save()
                    messages.success(request,"Account successfully created")
                    return render(request, 'authentication/login.html')


        return render(request, 'authentication/register.html')
    

# user login process. 
# to checks the provided username and password, 
# authenticates the user, 
# and logs them in if the credentials are valid.

class LoginView(View):
    def get(self,request):
        return render(request, 'authentication/login.html')
    
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']

        if username and password:

            user = auth.authenticate(username=username,password=password)

            if user:
                if user.is_active:
                    auth.login(request,user)
                    messages.success(request,'Welcome, '+user.username+' you are now logged in')
                    return redirect('preferences')


            messages.error(request,'invalid credentials please try again')
            return render(request, 'authentication/login.html')


        messages.error(request,'Please fill all fields')
        return render(request, 'authentication/login.html')


# logout process. 
# It logs the user out and redirects them to the login page.

class LogoutView(View):
    def post(self,request):
        auth.logout(request)
        messages.success(request,'You have been logged out')
        return redirect('login')




