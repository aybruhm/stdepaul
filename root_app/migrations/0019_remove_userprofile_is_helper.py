# Generated by Django 3.2 on 2022-12-12 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root_app', '0018_alter_helper_hours_of_operation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_helper',
        ),
    ]
