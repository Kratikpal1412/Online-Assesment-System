"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from faculty import views as faculty_views
from faculty.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, notificationCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register,name='register'),
    path('addexam/', PostListView.as_view(),name='addexam'),
    path('post5/<int:pk>/', PostDetailView.as_view(template_name='faculty/post5_detail.html'),name='post5-detail'),
    path('post/new/', PostCreateView.as_view(template_name='faculty/post_form.html'),name='post-create'),
    path('notification/new/', notificationCreateView.as_view(template_name='notification.html'),name='notification-create'),
    path('post/<int:pk>/update', PostDetailView.as_view(),name='post-update'),
    path('flogin/', auth_views.LoginView.as_view(template_name='blog/flogin.html'),name='flogin'),
    path('clogin/', auth_views.LoginView.as_view(template_name='blog/clogin.html'),name='clogin'),
     path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'),name='logout'),
    path('', include('blog.urls')),

]
