# Generated by Django 2.0 on 2019-12-17 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_land'),
    ]

    operations = [
        migrations.RenameField(
            model_name='land',
            old_name='piped_water',
            new_name='distance_to_main_road',
        ),
        migrations.RenameField(
            model_name='land',
            old_name='power_line',
            new_name='distance_to_piped_water',
        ),
        migrations.RenameField(
            model_name='land',
            old_name='road_access',
            new_name='distance_to_power_line',
        ),
    ]
