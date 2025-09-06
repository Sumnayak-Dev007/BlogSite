from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.


def index(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        
    else:
        form = SignUpForm()

    return render(request,'register.html',{'form':form})
