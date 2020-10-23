from django.urls import path
from .views import HomePageView, Cat1PageView, Cat2PageView, Cat3PageView, Cat4PageView, Cat5PageView, Cat1DetailView, SignUpView

urlpatterns = [
    path('cat1/', Cat1PageView.as_view(), name='cat1'),
    path('cat1/<int:pk>/', Cat1DetailView.as_view(), name='post_detail'),
    path('cat2/', Cat2PageView.as_view(), name='cat2'),
    path('cat3/', Cat3PageView.as_view(), name='cat3'),
    path('cat4/', Cat4PageView.as_view(), name='cat4'),
    path('cat5/', Cat5PageView.as_view(), name='cat5'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', HomePageView.as_view(), name='home'),
]