from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import UserSigninForm, UserSignupForm

# Create your views here.
def user_signup(request):
    form = UserSignupForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('User:signin')
    
    return render(request, 'signup.html', {'form': form})


def user_signin(request):
    
    form = UserSigninForm(request.POST or None)
 
    context = {
        'form': form,
        'errorCredentials': False,
        'status': request.GET.get('status')
    }
    
    if form.is_valid():
        user = authenticate(
            request,
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        if user is not None:
            login(request, user)
            return redirect('home:projects')
        
        context['errorCredentials'] = True
        
    return render(request, 'signin.html', context)
        
        
def user_logout(request):
    logout(request)
    return redirect('User:signin')