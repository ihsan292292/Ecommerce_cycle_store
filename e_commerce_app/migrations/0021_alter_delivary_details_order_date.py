# Generated by Django 3.2.12 on 2023-09-29 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0020_delivary_details_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivary_details',
            name='order_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]