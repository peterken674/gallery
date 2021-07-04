# Generated by Django 3.2.5 on 2021-07-04 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='country',
            field=models.CharField(default='Unknown', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
