# Generated by Django 3.2 on 2022-12-22 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0017_alter_wikientry_created_by'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='wikientry',
            unique_together={('title', 'location')},
        ),
    ]
