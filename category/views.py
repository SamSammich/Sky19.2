from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from category.models import Category


class CategoryCreateView(CreateView):
    model = Category
    fields = ('title', 'description',)
    success_url = reverse_lazy('category:list')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('title', 'description',)
    success_url = reverse_lazy('category:list')


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category:list')