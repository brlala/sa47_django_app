from django.urls import path
from .views import PostListView,PostDetailView
from . import views

# import all views to this url

# use unique naming convention as it may affect when we want to reroute
urlpatterns = [
    # path('', views.home, name='mysite-home'),
    path('', PostListView.as_view(), name='mysite-home'),
    path('restaurant/<str:pk>', PostDetailView.as_view(), name='restaurant-detail'),
    path('about/', views.about, name='mysite-about'),
]
