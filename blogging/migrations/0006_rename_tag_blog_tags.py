# Generated by Django 4.0.1 on 2022-03-07 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0005_blog_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='tag',
            new_name='tags',
        ),
    ]
