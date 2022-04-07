from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.home, name='home'),

	path('addPost/', views.addPost, name='addPost'),
	path('addComment/<str:pk>/', views.addComment, name='addComment'),
	path('addProfile', views.addProfile, name='addProfile'),

	path('register', views.registerUser, name='registerUser'),
	path('login', views.loginUser, name='login'),
	path('logout', views.logoutUser, name='logout'),
	path('userProfile/<str:pk>/', views.userProfile, name='userProfile'),

	path('likePost/<str:pk>', views.likePostOnHomePage, name='likePostHome'),
	path('likePost/<str:pk>', views.likePostOnUserProfilePage, name='likePostUserPage'),

	path('allComments/<str:pk>', views.allPostComments, name='allComments'),
]