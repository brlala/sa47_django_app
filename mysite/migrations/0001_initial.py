# Generated by Django 2.1.7 on 2019-03-01 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('rating', models.SmallIntegerField()),
                ('comment_datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notification_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('status', models.BinaryField()),
                ('recipient_id', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('reply_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('reply', models.TextField()),
                ('reply_datetime', models.DateTimeField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('restaurant_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('avg_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('phone_number', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('restaurant_picture', models.ImageField(default='restaurant.jpg', upload_to='../mysite/static/mysite/images/restaurant')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Category')),
            ],
        ),
        migrations.AddField(
            model_name='notification',
            name='reply',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mysite.Reply'),
        ),
        migrations.AddField(
            model_name='comment',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Restaurant'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]
