# Generated by Django 5.0.6 on 2024-06-29 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_id',
        ),
    ]
