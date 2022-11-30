# Generated by Django 4.1.3 on 2022-11-30 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='extended_info',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='production_year',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
