# Generated by Django 3.2 on 2022-12-12 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0005_alter_wikientry_hours_of_operation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikientry',
            name='title',
            field=models.CharField(default='Untitled', max_length=255),
        ),
    ]
