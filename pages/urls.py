from django.urls import path
from .views import ( 
    HomePageView, 
    SignUpView, 
    Cat1DeleteView, Cat2DeleteView, Cat3DeleteView, Cat4DeleteView, Cat5DeleteView,
    Cat1PageView, Cat2PageView, Cat3PageView, Cat4PageView, Cat5PageView, 
    Cat1DetailView, Cat2DetailView, Cat3DetailView, Cat4DetailView, Cat5DetailView, 
    Cat1CreateView, Cat2CreateView, Cat3CreateView, Cat4CreateView, Cat5CreateView, 
    Cat1CreateComment, Cat2CreateComment, Cat3CreateComment, Cat4CreateComment, Cat5CreateComment,
    Cat1UpdateView, Cat2UpdateView, Cat3UpdateView, Cat4UpdateView, Cat5UpdateView
)

from . import views

urlpatterns = [
    path('cat1/', Cat1PageView.as_view(), name='cat1'),
    path('cat1/<int:pk>/', Cat1DetailView.as_view(), name='post_detail'),
    path('cat1/<int:pk>/edit/', Cat1UpdateView.as_view(), name='post_edit'),
    path('cat1/<int:pk>/delete/', Cat1DeleteView.as_view(), name='post_delete'),
    path('cat1/comment/', Cat1CreateComment.as_view(), name='post_comment'),
    path('cat1/new/', Cat1CreateView.as_view(), name='post_new'),
    path('cat2/', Cat2PageView.as_view(), name='cat2'),
    path('cat2/<int:pk>/', Cat2DetailView.as_view(), name='post_detail2'),
    path('cat2/<int:pk>/edit/', Cat2UpdateView.as_view(), name='post_edit2'),
    path('cat2/<int:pk>/delete/', Cat2DeleteView.as_view(), name='post_delete2'),
    path('cat2/comment/', Cat2CreateComment.as_view(), name='post_comment2'),
    path('cat2/new/', Cat2CreateView.as_view(), name='post_new2'),
    path('cat3/', Cat3PageView.as_view(), name='cat3'),
    path('cat3/<int:pk>/', Cat3DetailView.as_view(), name='post_detail3'),
    path('cat3/<int:pk>/edit/', Cat3UpdateView.as_view(), name='post_edit3'),
    path('cat3/<int:pk>/delete/', Cat3DeleteView.as_view(), name='post_delete3'),
    path('cat3/comment/', Cat3CreateComment.as_view(), name='post_comment3'),
    path('cat3/new/', Cat3CreateView.as_view(), name='post_new3'),
    path('cat4/', Cat4PageView.as_view(), name='cat4'),
    path('cat4/<int:pk>/', Cat4DetailView.as_view(), name='post_detail4'),
    path('cat4/<int:pk>/edit/', Cat4UpdateView.as_view(), name='post_edit4'),
    path('cat4/<int:pk>/delete/', Cat4DeleteView.as_view(), name='post_delete4'),
    path('cat4/comment/', Cat4CreateComment.as_view(), name='post_comment4'),
    path('cat4/new/', Cat4CreateView.as_view(), name='post_new4'),
    path('cat5/', Cat5PageView.as_view(), name='cat5'),
    path('cat5/<int:pk>/', Cat5DetailView.as_view(), name='post_detail5'),
    path('cat5/<int:pk>/edit/', Cat5UpdateView.as_view(), name='post_edit5'),
    path('cat5/<int:pk>/delete/', Cat5DeleteView.as_view(), name='post_delete5'),
    path('cat5/comment/', Cat5CreateComment.as_view(), name='post_comment5'),
    path('cat5/new/', Cat5CreateView.as_view(), name='post_new5'),
    path('signup/', views.newsignup, name='signup'),
    path('', views.newsignup , name='home'),
]