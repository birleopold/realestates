# Generated by Django 2.0 on 2019-12-17 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20191028_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='for_sale',
            field=models.BooleanField(default=False),
        ),
    ]
