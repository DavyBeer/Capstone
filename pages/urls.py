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
    path('ExerciseQuestion/', Cat1PageView.as_view(), name='cat1'),
    path('ExerciseQuestion/<int:pk>/', Cat1DetailView.as_view(), name='post_detail'),
    path('ExerciseQuestion/<int:pk>/edit/', Cat1UpdateView.as_view(), name='post_edit'),
    path('ExerciseQuestion/<int:pk>/delete/', Cat1DeleteView.as_view(), name='post_delete'),
    path('ExerciseQuestion/comment/', Cat1CreateComment.as_view(), name='post_comment'),
    path('ExerciseQuestion/new/', Cat1CreateView.as_view(), name='post_new'),
    path('NutritionQuestion/', Cat2PageView.as_view(), name='cat2'),
    path('NutritionQuestion/<int:pk>/', Cat2DetailView.as_view(), name='post_detail2'),
    path('NutritionQuestion/<int:pk>/edit/', Cat2UpdateView.as_view(), name='post_edit2'),
    path('NutritionQuestion/<int:pk>/delete/', Cat2DeleteView.as_view(), name='post_delete2'),
    path('NutritionQuestion/comment/', Cat2CreateComment.as_view(), name='post_comment2'),
    path('NutritionQuestion/new/', Cat2CreateView.as_view(), name='post_new2'),
    path('EquipmentReviews/', Cat3PageView.as_view(), name='cat3'),
    path('EquipmentReviews/<int:pk>/', Cat3DetailView.as_view(), name='post_detail3'),
    path('EquipmentReviews/<int:pk>/edit/', Cat3UpdateView.as_view(), name='post_edit3'),
    path('EquipmentReviews/<int:pk>/delete/', Cat3DeleteView.as_view(), name='post_delete3'),
    path('EquipmentReviews/comment/', Cat3CreateComment.as_view(), name='post_comment3'),
    path('EquipmentReviews/new/', Cat3CreateView.as_view(), name='post_new3'),
    path('GymReviews/', Cat4PageView.as_view(), name='cat4'),
    path('GymReviews/<int:pk>/', Cat4DetailView.as_view(), name='post_detail4'),
    path('GymReviews/<int:pk>/edit/', Cat4UpdateView.as_view(), name='post_edit4'),
    path('GymReviews/<int:pk>/delete/', Cat4DeleteView.as_view(), name='post_delete4'),
    path('GymReviews/comment/', Cat4CreateComment.as_view(), name='post_comment4'),
    path('GymReviews/new/', Cat4CreateView.as_view(), name='post_new4'),
    path('CoachReviews/', Cat5PageView.as_view(), name='cat5'),
    path('CoachReviews/<int:pk>/', Cat5DetailView.as_view(), name='post_detail5'),
    path('CoachReviews/<int:pk>/edit/', Cat5UpdateView.as_view(), name='post_edit5'),
    path('CoachReviews/<int:pk>/delete/', Cat5DeleteView.as_view(), name='post_delete5'),
    path('CoachReviews/comment/', Cat5CreateComment.as_view(), name='post_comment5'),
    path('CoachReviews/new/', Cat5CreateView.as_view(), name='post_new5'),
    path('signup/', views.newsignup, name='signup'),
    path('', views.newsignup , name='home'),
]