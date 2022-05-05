from django.urls import path
from . import views

urlpatterns = []
urlpatterns +=[
    path('', views.index, name='index'),
    path('searchbar/', views.searchbar, name='searchbar'),
    path('stock/', views.ProductListView.as_view(), name='stock'),
    path('companies/', views.CompanyListView.as_view(), name='companies'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name = 'item-detail'),
    path('company/<int:pk>', views.CompanyDetailView.as_view(), name = 'company-detail'),
]


