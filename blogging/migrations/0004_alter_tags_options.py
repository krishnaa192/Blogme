# Generated by Django 4.0.1 on 2022-03-06 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0003_blog_blog_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tags',
            options={'ordering': ['created']},
        ),
    ]
