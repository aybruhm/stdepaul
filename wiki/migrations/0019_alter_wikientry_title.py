# Generated by Django 3.2 on 2022-12-22 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0018_alter_wikientry_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikientry',
            name='title',
            field=models.CharField(default='Untitled', max_length=255),
        ),
    ]
