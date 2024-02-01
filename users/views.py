from django.shortcuts import render,redirect
from .forms import NewRegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = NewRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('article:index')
    else:
        form = NewRegistrationForm()
    context ={
            'form':form
        }

    return render(request, 'users/register.html',context)

def profile(request):
    return render(request,'users/profile.html')