from django.shortcuts import render, redirect #Import render for templates and redirect for navigation
from django.contrib.auth import authenticate, login, logout #Import auth methods
from django.contrib.auth.decorators import login_required #Import decorator for secured views
from .forms import ContactForm, RegistrationForm, ArticleForm #Import forms defined in forms.py
from .models import Article #Import Article model from models.py


#Home page view
def home_view(request):
    return render(request, 'form_auth/home.html') #render the home.html template

#Contact form view
def contact_view(request):
    if request.method == 'POST': #Check if the user has filled out the ContactForm and submitted it.
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    
    else:
        form = ContactForm() # Create an empty form instance for GET requests

    return render(request, 'form_auth/contact.html', {'form': form}) # Render the contact page with the form


#Registration view
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=False) # Save the form without committing to the database yet
            user = form.save() #The form is saved as a User object.
            user.set_password(form.cleaned_data['password']) #set_password() hashes the user’s password (to securely store it).
            user.save() # Save the hashed password to the database
            return redirect('login') # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()  # Create an empty form for GET requests

    return render(request, 'form_auth/registration.html', {'form': form}) 
    # Render the register page with the form


# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username'] # Get the submitted username
        password = request.POST['password'] # Get the submitted password
        user = authenticate(request, username= username, password=password) # Authenticate the user
        if user: # If the user exists and credentials are correct
            login(request, user) # Log the user in
            return redirect('profile') # Redirect to the profile page
        
        else:
            return render(request, 'form_auth/login.html', {'error': 'Invalid credentials'}) #Show error msg
        
    return render(request, 'form_auth/login.html') # Render the login page for GET requests


# Logout View
def logout_view(request):
    logout(request) # Log the user out
    return redirect('login') # Redirect to the login page


# Secured profile page view
@login_required # Ensure the user is logged in to access this view
def profile_view(request):
    return render(request, 'form_auth/profile.html')

# Article creation view
@login_required # Ensure the user is logged in to access this view
def Article_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = ArticleForm()
    
    return render(request, 'form_auth/article.html', {'form': form})

