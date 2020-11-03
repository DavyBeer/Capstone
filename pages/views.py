from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import request
from .models import Cat1, Cat2, Cat3, Cat4, Cat5

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