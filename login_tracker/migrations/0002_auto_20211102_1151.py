# Generated by Django 3.2.9 on 2021-11-02 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginhistorytracker',
            name='browser',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='loginhistorytracker',
            name='host',
            field=models.CharField(max_length=256, null=True),
        ),
    ]