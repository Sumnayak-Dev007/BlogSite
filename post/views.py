from django.shortcuts import render,redirect
from .models import Category,Catblog
from django.contrib import messages
from .forms import PostForm
# Create your views here.
def index(request):
    cat = Catblog.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # IMPORTANT: match your actual field name
            post.author = request.user           # if your model uses "author"
            # post.auther = request.user         # if you accidentally named it "auther"
            post.save()
            form.save_m2m()  # only needed if you have M2M fields (e.g., tags)
            messages.success(request, "Post created successfully!")
            return redirect("/")  # redirect after saving
    else:
        form = PostForm()

    context = {
        "cat": cat,
        "form": form
    }
    return render(request,'index.html',context)


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

    return render(request,'catview.html',context)
    

def blog_view(request,c_slug,b_slug):
    return render(request,'blog.html')