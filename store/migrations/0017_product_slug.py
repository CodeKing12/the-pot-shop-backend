# Generated by Django 4.1.7 on 2023-03-17 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(auto_created=True, default='default', max_length=250),
            preserve_default=False,
        ),
    ]
