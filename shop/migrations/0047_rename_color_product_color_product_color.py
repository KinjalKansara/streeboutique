# Generated by Django 5.0.6 on 2024-07-14 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0046_alter_cart1_product_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_color',
            old_name='color',
            new_name='product_color',
        ),
    ]