# Generated by Django 4.2.7 on 2023-12-07 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='mota',
            field=models.TextField(blank=True),
        ),
    ]