from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
from django.http import HttpResponse
from django.shortcuts import redirect
from users.forms import  UserUpdateForm, ProfileUpdateForm
from .models import Post
from .models import Post3

def login(request):
	return render(request, 'blog/login.html')

def leftpanel(request):
	return render(request, 'blog/leftpanel.html')

def home(request):
    context = {
        'posts': Post3.objects.all()
    }
    return render(request, 'blog/home.html', context)	
class PostListView(ListView):
    model= Post3
    template_name='blog/home.html'
    context_object_name= 'posts'
    ordering= ['-date_posted']

class PostDetailView(DetailView):
    model= Post3

def report(request):
	return render(request, 'blog/report.html')

def examdetail(request):
	return render(request, 'blog/examdetail.html')

def assigment(request):
	return render(request, 'blog/assigment.html')	

def facultyleftpanel(request):
	return render(request, 'blog/facultyleftpanel.html')


def logout(request):
	return render(request, 'blog/logout.html')

def changepassword(request):
	return render(request, 'changepassword.html')

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'blog/profile.html', context)


def login_sucess(request):
	return render(request, 'blog/login_sucess.html')	
	
	# if request.user.groups.filter(name="admins").exists():
 #        # user is an admin
 #        return redirect('blog/addexam')
 #    else:
 #        return redirect("blog/home")


