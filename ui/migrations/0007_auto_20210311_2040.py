# Generated by Django 3.1.7 on 2021-03-11 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0006_auto_20210310_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.CharField(default='#', max_length=100),
        ),
    ]
