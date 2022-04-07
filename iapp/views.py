from django.shortcuts import render, redirect
from .models import*
from .forms import addPostForm, registerUserForm, addProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.


@login_required(login_url='login')
def home(request):
	all_posts = Post.objects.all().order_by('-date_added')

	
	context_dict = {

		'all_posts': all_posts,
	}

	return render(request, 'iapp/home.html', context_dict)

def allPostComments(request, pk):
	post = Post.objects.get(id=pk)
	allComments = Comment.objects.filter(post=pk).order_by('-date_added')

	context_dict = {

		'allComments': allComments,
		'post': post
	}
	return render(request, 'iapp/allComments.html', context_dict)
	


def registerUser(request):
	form = registerUserForm
	if request.method == 'POST':
		form = registerUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')

	context_dict = {

		'form':form
	}
	return render(request, 'iapp/register_user.html', context_dict)


def loginUser(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			print(username, password)
			return redirect('addProfile')
		else:
			return redirect('login')
			print('no user found')

	context_dict = {


	}
	return render(request, 'iapp/login.html', context_dict)


def logoutUser(request):
	
	logout(request)
	return redirect('login')



@login_required(login_url='login')
def addPost(request):
	form = addPostForm
	user = request.user
	if request.method == 'POST':
		form = addPostForm(request.POST, request.FILES)
		if form.is_valid():
			img = form.cleaned_data['postImage']
			desc = form.cleaned_data['postDescription']
			newPost = Post(image=img, description=desc, user=user)
			newPost.save()
			return redirect('home')


	context_dict = {

		'form': form
	}
	return render(request, 'iapp/addPost.html', context_dict)

def addComment(request, pk):
	post = Post.objects.get(id=pk)
	user=request.user
	if request.method == 'POST':
		comment_data = request.POST['content']
		newComment = Comment(user=user, post=post, content=comment_data)
		newComment.save()
		return HttpResponseRedirect(reverse('allComments', args=[str(pk)]))

	context_dict = {

	}
	return render(request, 'iapp/allComments.html', context_dict)


def addProfile(request):
	form = addProfileForm
	user = request.user
	if request.method == 'POST':
		form = addProfileForm(request.POST, request.FILES)
		if form.is_valid():
			avatar = form.cleaned_data['avatar']
			bio = form.cleaned_data['bio']
			website_url = form.cleaned_data['website_url']

			newProfile = Profile(user=user, avatar=avatar, bio=bio, connection_url=website_url)
			newProfile.save()
			return redirect('home')

	context_dict = {

		'form': form,
	}
	return render(request, 'iapp/addProfile.html', context_dict)


@login_required(login_url='login')
def likePostOnHomePage(request, pk):
	post = Post.objects.get(id=pk)
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
	return HttpResponseRedirect(reverse('home'))


@login_required(login_url='login')
def likePostOnUserProfilePage(request, pk):
	post = Post.objects.get(id=pk)
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
	return HttpResponseRedirect(reverse('userProfile', args=[str(pk)]))



@login_required(login_url='login')
def userProfile(request, pk):
	user = User.objects.get(id=pk)
	userName = user.username
	email = user.email
	firstName = user.first_name
	lastName = user.last_name

	user_X = Profile.objects.get(user=pk)
	# bio = user_X.bio
	# profilePic = user_X.avatar
	

	usersPosts = Post.objects.filter(user=pk).order_by('-date_added')
	

	context_dict = {

		'userName':userName,
		'email':email,
		'firstName':firstName,
		'lastName':lastName,

		'posts':usersPosts,
		# 'bio':bio,
		# 'avatar':profilePic,
		'userX': user_X,
		
	}
	return render(request, 'iapp/userProfile.html', context_dict)