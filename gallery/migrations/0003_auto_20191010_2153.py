# Generated by Django 2.2.6 on 2019-10-10 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20191007_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]