from django.urls import path
from .views import HomePageView, Cat1PageView, Cat2PageView, Cat3PageView, Cat4PageView, Cat5PageView, BlogDetailView

urlpatterns = [
    path('cat1/', Cat1PageView.as_view(), name='cat1'),
    path('cat2/', Cat2PageView.as_view(), name='cat2'),
    path('cat3/', Cat3PageView.as_view(), name='cat3'),
    path('cat4/', Cat4PageView.as_view(), name='cat4'),
    path('cat5/', Cat5PageView.as_view(), name='cat5'),
    path('cat1/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', HomePageView.as_view(), name='home'),
]