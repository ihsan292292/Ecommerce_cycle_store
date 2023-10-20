# Generated by Django 3.2.12 on 2023-09-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0014_wishlist_age_range'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('prod_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('bike_type', models.CharField(max_length=50)),
                ('age_range', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('noOfSpeed', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('file_image', models.FileField(upload_to='')),
            ],
        ),
    ]