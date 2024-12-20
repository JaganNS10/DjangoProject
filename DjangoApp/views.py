from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


# post = [
# {'author':'Jagan','title':'Python','content':'About Python','date_posted':'oct 5 2024'},
# {'author':'Hemanth','title':'PLC','content':'About PLC','date_posted':'oct 5 2024'}
# ]
# def HomePage(request):
# 	Dictionary = {
# 	'Posts':Post.objects.all(),
# 	'content2':{'Name':'Jagan'}
# 	}#we must pass anything as a dictionary not as a list
# 	return render(request,'DjangoApp/Home.html',Dictionary)


class PostListView(ListView):
	model = Post
	template_name = 'DjangoApp/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'Posts'
	ordering = ['-date_posted']
	paginate_by = 5

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title','content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	fields = ['title','content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class UserPostListView(ListView):
	model = Post
	template_name = 'DjangoApp/user_posts.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'Posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


def MainPage(request):
	return render(request,'DjangoApp/About.html',{'title':'Main-Page'})

def Base(request):
	Title = {'title':'BasePage'}
	return render(request,'DjangoApp/Base.html',Title)


# def HomePage(request):
# 	return HttpResponse("<h1>Welcome To Django</h1>")

# def MainPage(request):
# 	return HttpResponse("<marquee direction='right'>Welcome To Django Main Page</marquee>")




