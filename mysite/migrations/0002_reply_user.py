# Generated by Django 2.1.7 on 2019-03-03 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
            preserve_default=False,
        ),
    ]
