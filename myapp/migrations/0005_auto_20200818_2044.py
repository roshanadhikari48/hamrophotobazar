# Generated by Django 2.2.10 on 2020-08-19 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200818_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='cat',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='image',
            name='added_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
