from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    DetailView,
    CreateView, 
    UpdateView)

from .models import Notification
from .models import Restaurant, Category


# region Wang Yafeng
# replaced by class based view
def home(request):
    categories = Category.objects.all()
    restaurant_list = Restaurant.objects.all()
    query = request.GET.get("query")
    category = request.GET.get("category")
    if query != '' and category:
        restaurant_list = restaurant_list.filter(
            (Q(name__icontains=query)|
            Q(description__icontains=query)|
            Q(address__icontains=query)) &
             Q(category__category_id__iexact=category)
        ).distinct()

    elif query:
        restaurant_list = restaurant_list.filter(
            Q(name__icontains=query)|
            Q(description__icontains=query)|
            Q(address__icontains=query)
            )

    for restaurant in restaurant_list:
        rating_total = 0
        if restaurant.comment_set.all():
            count = restaurant.comment_set.all().count()
            for comment in restaurant.comment_set.all():
                rating_total += comment.rating
            rating_avg = rating_total / count
            restaurant.average = rating_avg

    paginator = Paginator(restaurant_list, 3)
    page = request.GET.get('page')
    try:
        restaurants = paginator.page(page)
    except PageNotAnInteger:
        restaurants=paginator.page(1)
    except EmptyPage:
        restaurants=paginator.page(paginator.num_pages)
        

    context = {
        'restaurant_list': restaurants,
        'categories': categories,
    }
    return render(request, 'mysite/home.html', context)

class RestaurantDetailView(DetailView):
    model = Restaurant

# class RestaurantCreateView(LoginRequiredMixin,CreateView):  
class RestaurantCreateView(CreateView):
    model = Restaurant
    fields = ['name', 'category', 'address', 'avg_price', 'phone_number',
              'description', 'start_time', 'end_time', 'restaurant_picture']

    #validation: only manager can create restaurant info
    # def test_func(self):
    #     if self.request.user=='manager': 
    #         return True
    #     return False

# class RestaurantUpdateView(LoginRequiredMixin,UpdateView):
class RestaurantUpdateView(UpdateView):
    model = Restaurant
    fields = ['name', 'category', 'address', 'avg_price', 'phone_number',
              'description', 'start_time', 'end_time', 'restaurant_picture']
    # def test_func(self):
    #     if self.request.user=='manager':
    #         return True
    #     return False


# endregion


# region Teh Li Heng
# region Detail View page
# class PostDetailView(DetailView):
#     model = Restaurant
def detail(request, pk):
    # restaurant = Restaurant.objects.get(id=pk)
    restaurant = get_object_or_404(Restaurant, pk=pk)
    # comments = restaurant.comment_set.all()
    # for comment in comments:
    #     comment.replies = comment.reply_set.all()

    context = {
        'restaurant': restaurant,
        # 'comments': comments,
    }
    return render(request, 'mysite/restaurant_detail_comment.html', context)


# endregion

# region About Page
members = [
    {
        'name': 'Gao Jiaxue',
        'chinese_name': '高佳雪'
    },
    {
        'name': 'Teh Li Heng',
        'chinese_name': '郑理衡',
        'nickname': 'Henry',
    },
    {
        'name': 'Wang Yafeng',
        'chinese_name': '王亚凤'
    },
]


def about(request):
    # items must be passed as dictionary into context
    context = {
        'members': members
    }
    return render(request, 'mysite/about.html', context)


# endregion


def Message(request):
    context = {
        'notification': Notification.objects.filter(recipient_id=request.user.id)
        # 'notification': Notification.objects.filter(recipient_id="1")
    }
    return render(request, 'mysite/notification.html', context)
