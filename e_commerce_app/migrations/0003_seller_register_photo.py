# Generated by Django 3.2.12 on 2023-09-12 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0002_add_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller_register',
            name='photo',
            field=models.FileField(default=1, upload_to='e_commerce_app/static/Uploaded_images'),
            preserve_default=False,
        ),
    ]
