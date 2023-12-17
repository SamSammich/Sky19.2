from django.urls import path

from category.apps import CategoryConfig
from category.views import CategoryCreateView, CategoryListView, CategoryDetailView, CategoryUpdateView, \
    CategoryDeleteView

app_name = CategoryConfig.name

urlpatterns = [
    path('create', CategoryCreateView.as_view(), name='create'),
    path('', CategoryListView.as_view(), name='list'),
    path('view/<int:pk>', CategoryDetailView.as_view(), name='view'),
    path('edit/<int:pk>', CategoryUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', CategoryDeleteView.as_view(), name='delete'),


]
