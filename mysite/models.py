from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from users.models import Profile as Profile


class Category(models.Model):
    category_id = models.CharField(max_length=6, primary_key=True)
    category = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'{self.category} Category'


class Restaurant(models.Model):
    restaurant_id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    avg_price = models.DecimalField(max_digits=6, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    description = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    restaurant_picture = models.ImageField(
        default='restaurant.jpg', upload_to='images/restaurant')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} Restaurant'

    def get_absolute_url(self):
        return reverse('restaurant-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    comment_id = models.CharField(max_length=6, primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.SmallIntegerField()
    comment_datetime = models.DateTimeField()

    class Meta:
        ordering = ['-comment_datetime']

    def __str__(self):
        return f'{self.comment} Comment'


# c.user.user.username
# c.comment_datetime
class Reply(models.Model):
    reply_id = models.CharField(max_length=6, primary_key=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply = models.TextField()
    reply_datetime = models.DateTimeField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Replies"
        ordering = ['-reply_datetime']

    def __str__(self):
        return f'{self.reply} Reply'


# r= Reply()
# r.reply_datetime

class Notification(models.Model):
    notification_id = models.CharField(max_length=6, primary_key=True)
    reply = models.OneToOneField(Reply, on_delete=models.CASCADE)
    url = models.URLField()
    status = models.BinaryField()
    recipient_id = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.notification_id} Notification'
