# Generated by Django 3.2.12 on 2023-09-29 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0023_alter_delivary_details_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivary_details',
            name='products_image',
            field=models.CharField(max_length=50),
        ),
    ]
