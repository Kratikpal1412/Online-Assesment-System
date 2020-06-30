from django.shortcuts import render
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView
)
from .models import Post5
from .models import Notification
def addexam(request):
	context = {
        'posts': Post5.objects.all()
    }
	return render(request, 'faculty/addexam.html', context)		

class PostListView(ListView):
	model= Post5
	template_name='faculty/addexam.html'
	context_object_name= 'posts'
	ordering= ['-date_posted']

class PostDetailView(DetailView):
	model= Post5

class notificationCreateView(CreateView):
	model= Notification
	fields= ['message']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostCreateView(CreateView):
	model= Post5
	fields= ['total_score', 'exam_name', 'subject_name', 'start_date', 'end_date', 'questions']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(UpdateView):
	model= Post5
	fields= ['total_score', 'exam_name', 'subject_name', 'start_date', 'end_date', 'questions']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)		

	

	# template_name='faculty/post_detail.html'
	

# Create your views here.
