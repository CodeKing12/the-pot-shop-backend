# Generated by Django 4.1.7 on 2023-03-25 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_product_aggregate_reviews_alter_review_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='aggregate_reviews',
            new_name='reviews_aggr',
        ),
    ]
