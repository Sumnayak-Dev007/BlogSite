from django.shortcuts import render,redirect
from .forms import SignUpForm,ProfileForm
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from post.models import Catblog
from .models import Profile
from django.contrib.auth.decorators import login_required
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
    

@login_required
def dashboard(request):
    profile = Profile.objects.filter(author=request.user).first()
    post = Catblog.objects.filter(author=request.user)
    return render(request,'dashboard.html',{'profile':profile,'post':post})


@login_required
def profile_edit(request):
    # Ensure the profile exists (create on the fly if needed)
    profile, created = Profile.objects.get_or_create(author=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("dashboard")  # change to your profile view name
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "profile_edit.html", {"form": form, "profile": profile})
