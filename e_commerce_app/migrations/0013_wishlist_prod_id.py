# Generated by Django 3.2.12 on 2023-09-20 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0012_auto_20230920_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='prod_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
