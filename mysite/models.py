from django.contrib.auth.models import User
from django.db import models
from users import models as users_models



class Category(models.Model):
    categoryid = models.CharField(max_length=6,primary_key=True)
    category = models.CharField(max_length=20)


    def __str__(self):
        return f'{self.category} Category'

class Restaurant(models.Model):
    restaurantid = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    avgprice = models.DecimalField(max_digits=6, decimal_places=2)
    phonenumber = models.CharField(max_length=15)
    description = models.TextField()
    starttime = models.TimeField()
    endtime = models.TimeField()
    restaurantpicture = models.ImageField(
        default='reataurant.jpg', upload_to='../mysite/static/mysite/images')

    def __str__(self):
        return f'{self.name} Restaurant'



class Comment(models.Model):
    commentid = models.CharField(max_length=6, primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(users_models.Profile,on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.SmallIntegerField()
    commentdatetime = models.DateTimeField()

    def __str__(self):
        return f'{self.comment} Comment'




class Reply(models.Model):
    replyid = models.CharField(max_length=6,primary_key=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply = models.TextField()
    replydatetime = models.DateTimeField()

    def __str__(self):
        return f'{self.reply} Reply'


class Notification(models.Model):
    notificationid = models.CharField(max_length=6,primary_key=True)
    reply = models.OneToOneField(Reply,on_delete=models.CASCADE)
    url = models.URLField()
    status = models.BinaryField()
    recipientid = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.notificationid} Notification'


