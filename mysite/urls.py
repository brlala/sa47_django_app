from django.urls import path
from .views import RestaurantCreateView
from . import views

# import all views to this url

# use unique naming convention as it may affect when we want to reroute
urlpatterns = [
    path('', views.home, name='mysite-home'),
    path('restaurant/<str:pk>', views.detail, name='restaurant-detail-comment'),
    path('restaurant/new/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('about/', views.about, name='mysite-about'),
    path('notification/', views.Message, name='mysite-notification'),
]
