# Generated by Django 4.1.2 on 2022-10-29 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.TextField(default=None, max_length=32),
            preserve_default=False,
        ),
    ]
