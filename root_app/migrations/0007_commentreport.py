# Generated by Django 3.2 on 2022-12-11 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('root_app', '0006_helper_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=10000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rule_broken', models.CharField(choices=[('ISILL', 'Is illegal'), ('ISAIM', 'Promotes AI/ML'), ('ISSPA', 'Is spam'), ('ISHAT', 'Is hate speech'), ('ISSCA', 'Is a scam'), ('INAPP', 'Is Inappropriate'), ('OTHER', 'Other')], max_length=255)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root_app.comment')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
