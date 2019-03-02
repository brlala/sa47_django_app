from django.shortcuts import render
from .models import Restaurant, Category, Comment
from django.views.generic import DetailView
from django.db.models import Q


# replaced by class based view
def home(request):
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all().order_by('name')
    query = request.GET.get("query")
    category = request.GET.get("category")
    if query != '' and category:
        restaurants = restaurants.filter(
            (Q(name__icontains=query) &
             Q(category__category_id__iexact=category))
        ).distinct()

    elif query:
        restaurants = restaurants.filter(Q(name__icontains=query))

    for restaurant in restaurants:
        rating_total = 0
        if restaurant.comment_set.all():
            count = restaurant.comment_set.all().count()
            for comment in restaurant.comment_set.all():
                rating_total += comment.rating
            rating_avg = rating_total / count
            restaurant.average = rating_avg

    context = {
        'restaurants': restaurants,
        'categories': categories,
    }
    return render(request, 'mysite/home.html', context)


# using generic django Class based views, what models to query
# class PostListView(ListView):
#     model = Restaurant
#     template_name = 'mysite/home.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['name']

# region Teh Li Heng
# region Detail View page
class PostDetailView(DetailView):
    model = Restaurant


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
# endregion
