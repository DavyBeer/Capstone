from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.views import generic
from django.http import request
from django.shortcuts import render
from .models import Cat1, Cat2, Cat3, Cat4, Cat5, Comment, Comment2, Comment3, Comment4, Comment5

class HomePageView(TemplateView):
    template_name = 'home.html'

class Cat1PageView(ListView):
    model = Cat1
    template_name = 'list.html'

class Cat2PageView(ListView):
    model = Cat2
    template_name = 'list.html'

class Cat3PageView(ListView):
    model = Cat3
    template_name = 'list.html'

class Cat4PageView(ListView):
    model = Cat4
    template_name = 'list.html'

class Cat5PageView(ListView):
    model = Cat5
    template_name = 'list.html'

class Cat1DetailView(DetailView):
    model = Cat1
    context_object_name = 'post'
    template_name = 'post_detail.html'

class Cat2DetailView(DetailView):
    model = Cat2
    context_object_name = 'post'
    template_name = 'post_detail.html'

class Cat3DetailView(DetailView):
    model = Cat3
    context_object_name = 'post'
    template_name = 'post_detail.html'

class Cat4DetailView(DetailView):
    model = Cat4
    context_object_name = 'post'
    template_name = 'post_detail.html'

class Cat5DetailView(DetailView):
    model = Cat5
    context_object_name = 'post'
    template_name = 'post_detail.html'

class Cat1CreateView(CreateView):
    model = Cat1
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class Cat2CreateView(CreateView):
    model = Cat2
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class Cat3CreateView(CreateView):
    model = Cat3
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class Cat4CreateView(CreateView):
    model = Cat4
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class Cat5CreateView(CreateView):
    model = Cat5
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class Cat1CreateComment(CreateView):
    model = Comment
    template_name = 'post_comment.html'
    fields = ['article', 'comment', 'author']

class Cat2CreateComment(CreateView):
    model = Comment2
    template_name = 'post_comment.html'
    fields = ['article', 'comment', 'author']

class Cat3CreateComment(CreateView):
    model = Comment3
    template_name = 'post_comment.html'
    fields = ['article', 'comment', 'author']

class Cat4CreateComment(CreateView):
    model = Comment4
    template_name = 'post_comment.html'
    fields = ['article', 'comment', 'author']

class Cat5CreateComment(CreateView):
    model = Comment5
    template_name = 'post_comment.html'
    fields = ['article', 'comment', 'author']

class Cat1UpdateView(UpdateView):
    model = Cat1
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class Cat2UpdateView(UpdateView):
    model = Cat2
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class Cat3UpdateView(UpdateView):
    model = Cat3
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class Cat4UpdateView(UpdateView):
    model = Cat4
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class Cat5UpdateView(UpdateView):
    model = Cat5
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class Cat1DeleteView(DeleteView):
    model = Cat1
    context_object_name = 'post'
    template_name = 'post_delete.html'
    success_url = reverse_lazy('cat1')

class Cat2DeleteView(DeleteView):
    model = Cat2
    context_object_name = 'post'
    template_name = 'post_delete.html'
    success_url = reverse_lazy('cat2')

class Cat3DeleteView(DeleteView):
    model = Cat3
    context_object_name = 'post'
    template_name = 'post_delete.html'
    success_url = reverse_lazy('cat3')

class Cat4DeleteView(DeleteView):
    model = Cat4
    context_object_name = 'post'
    template_name = 'post_delete.html'
    success_url = reverse_lazy('cat4')

class Cat5DeleteView(DeleteView):
    model = Cat5
    context_object_name = 'post'
    template_name = 'post_delete.html'
    success_url = reverse_lazy('cat5')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def newsignup(request):
    if request.method=="POST":
        if request.POST.get('password1')==request.POST.get('password2'):
            try: 
                saveuser=User.objects.create_user(request.POST.get('username'),password=request.POST.get('password1'))
                saveuser.save()
                return render(request, 'base.html', {"form":UserCreationForm(), "info":"The User "+request.POST.get('username')+" is created successfully!"})
            except IntegrityError:
                return render(request, 'base.html', {"form":UserCreationForm(), "error":"The User "+request.POST.get('username')+" is already taken!"})
        else:
            return render(request, 'base.html', {"form":UserCreationForm(), "error":"The passwords are not mathcing!"})
    else:
        return render(request, 'base.html', {"form":UserCreationForm})