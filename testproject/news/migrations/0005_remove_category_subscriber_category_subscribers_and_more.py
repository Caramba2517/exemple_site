# Generated by Django 4.1.3 on 2022-11-22 17:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0004_alter_category_subscriber_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subscriber',
        ),
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(blank=True, max_length=200, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='SubscriberCategory',
        ),
    ]