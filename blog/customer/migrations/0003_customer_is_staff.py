# Generated by Django 4.0.6 on 2022-07-11 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_groups_customer_is_superuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
