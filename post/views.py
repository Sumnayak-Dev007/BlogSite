from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import Category,Catblog
from django.contrib import messages
from .forms import PostForm, CommentForm
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
    category = get_object_or_404(Category, slug=slug, status=0)
    posts = Catblog.objects.filter(category=category)

    # else:
    #     messages.error(request, "Something went wrong. Please try again.")
    #     return redirect('categories')

    context = {
        'cat':category,
        'posts' : posts
    }

    return render(request,'catview.html',context)
    

def blog_view(request,cat_slug, post_slug):
    if(Category.objects.filter(slug=cat_slug)):
        if(Catblog.objects.filter(slug=post_slug)):
            post = Catblog.objects.filter(slug=post_slug).first()
        else:
            messages.error(request, "Something went wrong. Please try again.")
            return redirect('catView')
    else:
        messages.error(request, "Something went wrong. Please try again.")
        return redirect('catView')

    if request.method == "POST":
        # if not request.user.is_authenticated:
        #     messages.warning(request, "Please log in to send a message.")
        #     login_url = f"{redirect('new_login').url}?{urlencode({'next': request.path})}"  # Preserve return URL
        #     return redirect(login_url)
        
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.author = request.user
            instance.post = post
            instance.save()
            return redirect('blog_view',cat_slug=cat_slug,post_slug=post_slug)
    else:
        c_form = CommentForm()


    context={
        'post':post,
        'c_form':c_form
    }

    

    return render(request,'blog.html',context)