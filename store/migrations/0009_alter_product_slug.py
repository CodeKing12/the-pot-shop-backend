# Generated by Django 4.1.7 on 2023-03-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(auto_created=True, max_length=250, unique=True),
        ),
    ]