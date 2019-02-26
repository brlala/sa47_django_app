from django.shortcuts import render
# from .models import Post

# this is the logic how we want to handle when people go to our homepage, we need to map the url and function at urls.py in the project
posts = [
    {
        'name': 'McDonald',
        'rating': 4.5,
        'description': 'This is a fast food restaurant',
        'image': '[insert image here]',
        'address': '352 Clementi Ave 2, #01-153, Singapore 120352',
        'contact': '6778 2223',
    },
    {
        'name': 'KFC',
        'rating': 4.3,
        'description': 'This is a fast food restaurant 2',
        'image': '[insert image here]',
        'address': '379 Clementi Ave 5',
        'contact': '6778 4441',
    }
]


def home(request):
    context = {
        # 'posts': Post.objects.all() #replace with this once database is created
        'posts': posts
    }
    return render(request, 'mysite/home.html', context)


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
