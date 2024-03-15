from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForms,RegisterForm,Profile
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import User

def LogIn(request):
    form = None  # Initialize the form variable outside the if block
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('product:index'))
    
    form = LoginForms()  # Instantiate the form for GET requests

    data = {
        'form': form  # Pass form to the template context
    }
    return render(request, 'login/login.html', context=data)

def signup(request):
    return render(request, 'signup/signup.html')

def logOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def register(request):
    if request.method == 'POST':
        password = request.POST["password1"]
        confirmation = request.POST["password2"]
        if password != confirmation:
            return render(request, "signup/signup.html", {
                "message": "Passwords must match."
        })
        form = RegisterForm(request.POST)

        if form.is_valid():
            try:
                user=User()
                user.username=form.cleaned_data['username']
                user.first_name=form.cleaned_data['first_name']
                user.last_name=form.cleaned_data['last_name']
                user.email=form.cleaned_data['email']
                user.set_password(form.cleaned_data['password1'])
                user.photo=form.cleaned_data['photo']
                user.save()
                return HttpResponseRedirect(reverse('login'))
            except:
                return HttpResponseRedirect(reverse('product:index'))
            
    form = RegisterForm()

    data = {
        'form': form 
    }
    return render(request, 'signup/signup.html',context=data)

class ProfileView(UpdateView):
    form_class=Profile
    model=User

    template_name='profile/profile.html'
    def get_object(self,queryset=None):
        return self.request.user
    def get_success_url(self):
        return reverse_lazy('index')

    
