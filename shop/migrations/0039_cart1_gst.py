# Generated by Django 4.2.5 on 2024-07-13 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0038_alter_cart1_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart1',
            name='gst',
            field=models.IntegerField(default=None),
        ),
    ]