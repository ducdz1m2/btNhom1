# Generated by Django 4.2.7 on 2023-12-08 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='isHot',
            field=models.BooleanField(default=False),
        ),
    ]
