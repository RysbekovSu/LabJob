# Generated by Django 4.1.3 on 2022-12-07 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser2', '0004_remove_news_description_remove_news_published_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='link',
            field=models.CharField(default='', max_length=100),
        ),
    ]
