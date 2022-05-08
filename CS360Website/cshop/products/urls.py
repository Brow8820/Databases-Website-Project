from django.urls import path
from . import views

urlpatterns = []
urlpatterns +=[
    path('', views.index, name='index'),
    path('searchbar/', views.searchbar, name='searchbar'),
    path('addwish/<int:pk>', views.addwish, name= 'addwish'),
    path('stock/', views.ProductListView.as_view(), name='stock'),
    path('stock100/', views.Product100.as_view(), name='stock100'),
    path('stock101/', views.Product500.as_view(), name='stock101'),
    path('stock102/', views.Product2000.as_view(), name='stock102'),
    path('stock103/', views.Product5000.as_view(), name='stock103'),
    path('stock104/', views.Product5001.as_view(), name='stock104'),
    path('wishlist/', views.ProductwList.as_view(), name='stock999'),
    path('companies/', views.CompanyListView.as_view(), name='companies'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name = 'item-detail'),
    path('company/<int:pk>', views.CompanyDetailView.as_view(), name = 'company-detail'),
]


