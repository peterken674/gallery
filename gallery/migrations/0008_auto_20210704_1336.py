# Generated by Django 3.2.5 on 2021-07-04 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_remove_location_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ManyToManyField(null=True, to='gallery.Category'),
        ),
    ]
