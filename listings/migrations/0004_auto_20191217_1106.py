# Generated by Django 2.0 on 2019-12-17 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listing_for_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='for_sale',
            field=models.BooleanField(default=True),
        ),
    ]
