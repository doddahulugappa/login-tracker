# Generated by Django 3.2.9 on 2021-11-02 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_tracker', '0003_loginhistorytracker_user_agent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loginhistorytracker',
            name='browser',
        ),
    ]
