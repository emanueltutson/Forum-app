# Generated by Django 4.1.5 on 2023-01-11 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='like'),
        ),
    ]