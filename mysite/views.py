from django.http import HttpResponse
from django.shortcuts import render

# this is the logic how we want to handle when people go to our homepage, we need to map the url and function at urls.py in the project
def home(request):
    return render(request, 'mysite/home.html')

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'mysite/about.html')
