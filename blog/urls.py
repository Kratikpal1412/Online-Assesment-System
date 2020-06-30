from django.urls import path
from .views import PostListView, PostDetailView
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.login, name='blog-login'),
    path('leftpanel/', views.leftpanel, name='blog-lefpanel'),
    path('home/', PostListView.as_view(), name='blog-home'),
    path('home/post3/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('report/', views.report, name='blog-report'),
    path('examdetail/', views.examdetail, name='blog-examdetail'),
    path('assigment/', views.assigment, name='blog-assigment'),
    path('changepassword/', views.changepassword, name='blog-changepassword'),
    path('facultyleftpanel/', views.facultyleftpanel, name='blog-facultyleftpanel'),
    path('login_sucess/', views.login_sucess, name='blog-login_sucess'),
    path('profile/', views.profile, name='blog-profile'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)