# Generated by Django 3.2.12 on 2023-09-29 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0022_alter_delivary_details_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivary_details',
            name='products_image',
            field=models.FileField(upload_to='e_commerce_app/static/Orderd_products'),
        ),
    ]
