# Generated by Django 5.0.6 on 2024-07-14 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0043_alter_cart1_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart1',
            old_name='color',
            new_name='product_color',
        ),
    ]
