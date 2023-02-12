# Generated by Django 3.2.4 on 2023-02-11 18:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='UnTitled', max_length=200)),
                ('description', models.CharField(default='Author not provied any description', max_length=200)),
                ('content', models.CharField(default='Author not provied any description', max_length=2000)),
                ('blog_profile_img', models.CharField(default='https://www.equalityhumanrights.com/sites/default/files/styles/listing_image/public/default_images/blog-teaser-default-full_5.jpg?itok=YOsTg-7X', max_length=2000)),
                ('categories', models.CharField(max_length=200)),
                ('updated_date', models.DateField(default=datetime.datetime(2023, 2, 11, 18, 1, 30, 525614, tzinfo=utc))),
            ],
        ),
    ]
