# Generated by Django 3.0.1 on 2020-01-02 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='desc',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
