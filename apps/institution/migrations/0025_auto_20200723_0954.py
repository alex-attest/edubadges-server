# Generated by Django 2.2.14 on 2020-07-23 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0024_auto_20200615_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
