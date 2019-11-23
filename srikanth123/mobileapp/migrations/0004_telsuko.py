# Generated by Django 2.2.6 on 2019-11-23 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileapp', '0003_anand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telsuko',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
