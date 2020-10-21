from django.views.generic import TemplateView, ListView, DetailView
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

class BlogDetailView(DetailView):
    model = Cat1
    template_name = 'post_detail.html'