from django.urls import path
from .views import (
    RestaurantDetailView,
    RestaurantCreateView,
    RestaurantUpdateView)
from . import views

# import all views to this url

# use unique naming convention as it may affect when we want to reroute
urlpatterns = [
    path('', views.home, name='mysite-home'),
    path('restaurant/new/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('restaurant/<str:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('restaurant/article/<str:pk>', views.detail, name='restaurant-detail-comment'),
    path('restaurant/<str:pk>/update', RestaurantUpdateView.as_view(), name='restaurant-update'),
    path('about/', views.about, name='mysite-about'),
    path('notification/', views.Message, name='mysite-notification'),
]
