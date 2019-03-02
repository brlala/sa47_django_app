from django.shortcuts import render
from .models import Restaurant,Category

# this is the logic how we want to handle when people go to our homepage, we need to map the url and function at urls.py in the project
# posts = [
#     {
#         'name': 'McDonald',
#         'rating': 4.5,
#         'description': 'This is a fast food restaurant',
#         'image': '[insert image here]',
#         'address': '352 Clementi Ave 2, #01-153, Singapore 120352',
#         'contact': '6778 2223',
#     },
#     {
#         'name': 'KFC',
#         'rating': 4.3,
#         'description': 'This is a fast food restaurant 2',
#         'image': '[insert image here]',
#         'address': '379 Clementi Ave 5',
#         'contact': '6778 4441',
#     }
# ]
from django.views.generic import ListView

from .models import Restaurant


# # this is the logic how we want to handle when people go to our homepage, we need to map the url and function at urls.py in the project
# posts = [
#     {
#         'name': 'McDonald',
#         'rating': 4.5,
#         'description': 'This is a fast food restaurant',
#         'image': '[insert image here]',
#         'address': '352 Clementi Ave 2, #01-153, Singapore 120352',
#         'contact': '6778 2223',
#     },
#     {
#         'name': 'KFC',
#         'rating': 4.3,
#         'description': 'This is a fast food restaurant 2',
#         'image': '[insert image here]',
#         'address': '379 Clementi Ave 5',
#         'contact': '6778 4441',
#     }
# ]

# replaced by class based view
def home(request):
    categories=Category.objects.all()
    restaurants=Restaurant.objects.all()
    query=request.GET.get("q")
    if query:
        restaurants=restaurants.filter(name_icontains=query)

    context = {
        'posts': restaurants,
        'categories':categories
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