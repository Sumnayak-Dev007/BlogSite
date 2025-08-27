from django.shortcuts import render
from .models import Category,Catblog
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')


def categories(request):
    categories = Category.objects.filter(status = 0)
    context={
        'categories':categories
    }
    return render(request,'categories.html',context)


def catView(request,slug):
    if(Category.objects.filter(slug=slug)):
        cat = Category.objects.filter(slug=slug,status=0)

    else:
        messages.error(request, "Something went wrong. Please try again.")
        return redirect('categories')

    context = {
        'cat':cat
    }

    return render(request,'blog.html',context)
    