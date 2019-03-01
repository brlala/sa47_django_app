from django.contrib import admin
from mysite.models import Category, Reply, Restaurant, Comment, Notification

admin.site.register(Category)
admin.site.register(Restaurant)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Notification)
