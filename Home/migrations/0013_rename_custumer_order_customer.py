# Generated by Django 4.2.7 on 2023-12-08 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_alter_customer_options_alter_customer_managers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='custumer',
            new_name='customer',
        ),
    ]
