# Generated by Django 4.0.4 on 2022-05-22 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_rename_mail_profile_gmail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gmail',
        ),
    ]
