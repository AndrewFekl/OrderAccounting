# Generated by Django 3.2.10 on 2021-12-09 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_orders_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
