# Generated by Django 3.1.7 on 2021-03-10 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0002_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='description',
            new_name='message',
        ),
    ]