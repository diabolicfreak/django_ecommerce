from django.http import HttpResponse
from django.contrib.auth import login, authenticate, get_user_model
from .forms import ContactForm, LoginForm, RegisterForm
from django.shortcuts import render, redirect
User = get_user_model()

def home_page(request):
    return render(request, 'home.html')

def contact_page(request):
    print('request.method ', request.method)
    form = ContactForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print('form.clean', form.cleaned_data)
        context['form'] = ContactForm()
    return render(request, 'contact/view.html', context=context)

def login_page(request):
    context = {}
    form = LoginForm(request.POST or None)
    context['form'] = form
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('is_authenticated',request.user.is_authenticated())
        if not request.user.is_authenticated():
            user = authenticate(request=request, username=username, password=password)
            if user:
                login(request, user)
                # context['form'] = LoginForm()
                print('is_authenticated',request.user.is_authenticated())
                return redirect('/')
            else:
                print("Authentication Error")
                return render(request, 'auth/login.html', context=context)
    return render(request, 'auth/login.html', context=context)

def register_page(request):
    context = {}
    form = RegisterForm(request.POST or None)
    context['form'] = form
    if form.is_valid():
        username = form.cleaned_data.get('username') 
        email = form.cleaned_data.get('email') 
        password = form.cleaned_data.get('password') 
        user = User.objects.create(username=username, email=email, password=password)
    return render(request, 'auth/register.html', context=context)
