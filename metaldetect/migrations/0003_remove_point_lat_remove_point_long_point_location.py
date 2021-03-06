# Generated by Django 4.0.2 on 2022-02-13 18:12

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('metaldetect', '0002_pointgroup_color_pointgroup_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='point',
            name='long',
        ),
        migrations.AddField(
            model_name='point',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63, null=True),
        ),
    ]
