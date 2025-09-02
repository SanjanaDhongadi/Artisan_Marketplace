from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.db import connection
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.middleware.csrf import get_token
from django.core.exceptions import ObjectDoesNotExist  # Import ObjectDoesNotExist exception
from .models import Profile

def index(request):
    return render(request,'index.html')


def intro(request):
    return render(request,'intro.html')

def pottery(request):
    return render(request, 'pottery.html')

def add_to_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_price = request.POST.get('item_price')
        # You can handle the cart logic here, like adding the item to the session or database
    return redirect('potte`ry')  # Redirect to the home page after adding to cart

def soft(request):
    return render(request, 'soft.html')

def add_to_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_price = request.POST.get('item_price')
        # You can handle the cart logic here, like adding the item to the session or database
    return redirect('soft')  # Redirect to the home page after adding to cart

def wall_stickers(request):
    return render(request, 'wall_stickers.html')

def add_to_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_price = request.POST.get('item_price')
        # You can handle the cart logic here, like adding the item to the session or database
    return redirect('wall_stickers')  # Redirect to the home page after adding to cart

def watch(request):
    return render(request, 'watch.html')

def add_to_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_price = request.POST.get('item_price')
        # You can handle the cart logic here, like adding the item to the session or database
    return redirect('watch')  # Redirect to the home page after adding to cart

def jewelry(request):
    return render(request, 'jewelry.html')

def add_to_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_price = request.POST.get('item_price')
        # You can handle the cart logic here, like adding the item to the session or database
    return redirect('jewelry')  # Redirect to the home page after adding to cart

def home_decor(request):
    return render(request, 'home_decor.html')

def add_to_cart(request):
    from django.shortcuts import redirect

def add_to_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_price = request.POST.get('item_price')
        # Handle adding the item to the cart logic here (e.g., session, database)
        # For example, you can add the item to the session
        if 'cart' not in request.session:
            request.session['cart'] = []
        request.session['cart'].append({'name': item_name, 'price': item_price})
    return redirect('products_page')  # Redirect to the products page after adding to cart


def invoice(request):
    return render(request, 'invoice.html')


def log(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)  # Logging in the user
            return redirect('index')
        else:
            return render(request, 'log.html', {'email': email, 'csrf_token': get_token(request)})  # Pass CSRF token back to the form for security

    return render(request, 'log.html', {'csrf_token': get_token(request)})



@login_required
def profile(request):
    user = request.user  # Get the current logged-in user
    context = {'user': user}  # Pass the user object to the template context
    
    return render(request, 'profile.html', context)
 

def terms(request):
    return render(request,'terms.html')

def about(request):
    return render(request,'about.html')

def return_policy(request):
    return render(request,'return_policy.html')

def privacy(request):
    return render(request,'privacy.html')   
        
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        age = request.POST.get('age')
        password = request.POST.get('password')
        
        hashed_password = make_password(password)  # Hash the password
        
        user = CustomUser.objects.create(username=name, email=email, mobile=mobile, age=age, password=hashed_password, name=name)

        if user is not None:
            login(request, user)  # Log in the user after registration
            return redirect('index')
        else:
            return render(request, 'register.html', {'csrf_token': get_token(request)})  # Pass CSRF token back to the form for security

    return render(request, 'register.html', {'csrf_token': get_token(request)})