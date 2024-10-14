from django.shortcuts import render
from .models import EducationProduct
from .models import PricingPost
from.models import StaffPost
from.models import NewsPost
from.models import GalleryPost
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm
from .forms import CustomLoginForm
from django.contrib.auth import logout
from django.core.mail import send_mail

# Create your views here.

def index(request):
    products = EducationProduct.objects.order_by('-created_date')[:3]
    posts = PricingPost.objects.order_by('-created_date')[:3]
    context = {
        'products': products,
        'posts': posts  
    }

    return render(request, 'pages/index.html', context)

def elements(request):

    return render (request, 'pages/elements.html',)

def staff(request):
    teachers = StaffPost.objects.order_by('-created_date')
    context = {
        'teachers' : teachers
    }
    return render (request, 'pages/staff.html', context)

def news(request):
    news = NewsPost.objects.order_by('created_date')

    context = {
        'news' : news
    }

    return render (request, 'pages/news.html', context)

def gallery(request):
    collections = GalleryPost.objects.order_by('created_date')

    context = {
        'collections' : collections
    }
    return render (request, 'pages/gallery.html', context)

def about(request):
    teachers = StaffPost.objects.order_by('-created_date')
    context = {
        'teachers' : teachers
    }
    return render (request, 'pages/about.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email through Mailtrap
            send_mail(
                f"{subject} - from {name} ({email})",  # Subject line
                message,  # Message body
                'no-reply@yourdomain.com',  # From email address (change to a valid email)
                ['tomhizb12@gmail.com'],  # Recipient email address (your own email)
                fail_silently=False,
            )

            # Success message
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact_us')  # Make sure 'contact_us' matches your URL pattern name
    else:
        form = ContactForm()
    
    return render(request, 'pages/contact.html', {'form': form})





def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Save user but don't commit to the database yet
            user.is_staff = True  # Grant admin access (optional)
            user.save()  # Now save the user instance to the database
            
            # Send email to the registered user
            send_mail(
                'Welcome to Our Platform!',  # Email subject
                'Thank you for registering with us!',  # Email message body
                'your_email@domain.com',  # From email (replace with your email)
                [user.email],  # To email (user's email from the form)
                fail_silently=False,
            )
            
            messages.success(request, 'Registration successful! A confirmation email has been sent to your email.')
            return redirect('admin:index')  # Redirect after registration
    else:
        form = CustomUserCreationForm()  # Render an empty form for GET request
    
    return render(request, 'pages/register.html', {'form': form})  # Always return an HttpResponse


def user_login(request):  
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if form.cleaned_data.get('remember_me'):
                request.session.set_expiry(1209600)  # 2 weeks
            else:
                request.session.set_expiry(0)  # Browser session
            messages.success(request, 'You have successfully logged in!')  
            return redirect('admin:index')  # Redirect to desired page
    else:
        form = CustomLoginForm()

    return render(request, 'pages/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('login')  # Redirect to your desired page

# def course_details(request, id):
#     more =  get_object_or_404(EducationProduct, id=id)
#     context = {
#         'more' : more
#     }
#     return render(request, 'pages/course_details.html', context)
