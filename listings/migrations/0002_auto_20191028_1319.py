# Generated by Django 2.2.6 on 2019-10-28 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='city',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='state',
            new_name='town',
        ),
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.IntegerField(),
        ),
    ]
