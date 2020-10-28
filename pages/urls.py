from django.urls import path
from .views import HomePageView, Cat1PageView, Cat2PageView, Cat3PageView, Cat4PageView, Cat5PageView, Cat1DetailView, Cat2DetailView, Cat3DetailView, Cat4DetailView, Cat5DetailView, SignUpView, Cat1CreateView, Cat2CreateView, Cat3CreateView, Cat4CreateView, Cat5CreateView

urlpatterns = [
    path('cat1/', Cat1PageView.as_view(), name='cat1'),
    path('cat1/<int:pk>/', Cat1DetailView.as_view(), name='post_detail'),
    path('cat1/new/', Cat1CreateView.as_view(), name='post_new'),
    path('cat2/', Cat2PageView.as_view(), name='cat2'),
    path('cat2/<int:pk>/', Cat2DetailView.as_view(), name='post_detail2'),
    path('cat2/new/', Cat2CreateView.as_view(), name='post_new'),
    path('cat3/', Cat3PageView.as_view(), name='cat3'),
    path('cat3/<int:pk>/', Cat3DetailView.as_view(), name='post_detail3'),
    path('cat3/new/', Cat3CreateView.as_view(), name='post_new'),
    path('cat4/', Cat4PageView.as_view(), name='cat4'),
    path('cat4/<int:pk>/', Cat4DetailView.as_view(), name='post_detail4'),
    path('cat4/new/', Cat4CreateView.as_view(), name='post_new'),
    path('cat5/', Cat5PageView.as_view(), name='cat5'),
    path('cat5/<int:pk>/', Cat5DetailView.as_view(), name='post_detail5'),
    path('cat5/new/', Cat5CreateView.as_view(), name='post_new'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', HomePageView.as_view(), name='home'),
]