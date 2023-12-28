from django.urls import path

from catalogapp.apps import CatalogappConfig
from catalogapp.views import contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, toggle_activity

app_name = CatalogappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('create/', ProductCreateView.as_view(), name="create_product"),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name="update_product"),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name="delete_product"),
    path('activity/<int:pk>/', toggle_activity, name="toggle_activity"),
    path('version/create/', VersionCreateView.as_view(), name='create_version'),
    path('version/update/', VersionUpdateView.as_view(), name='update_version'),
]
