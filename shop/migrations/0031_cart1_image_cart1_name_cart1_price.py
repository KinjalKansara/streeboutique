# Generated by Django 4.2.5 on 2024-07-12 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_rename_cart_cart1'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart1',
            name='image',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='cart1',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='cart1',
            name='price',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
