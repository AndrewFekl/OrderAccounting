# Generated by Django 3.1 on 2021-12-10 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20211210_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.customer'),
        ),
    ]
