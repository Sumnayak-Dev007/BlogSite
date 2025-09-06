from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth.views import LogoutView
from django.contrib import messages
# Create your views here.


def index(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = SignUpForm()

    return render(request,'register.html',{'form':form})


class CustomLogout(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request,"You have been Logged Out successfully!")
        return super().dispatch(request, *args, **kwargs)
    
