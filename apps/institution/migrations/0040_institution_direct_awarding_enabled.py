# Generated by Django 2.2.18 on 2021-03-23 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0039_auto_20210224_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='direct_awarding_enabled',
            field=models.BooleanField(default=False),
        ),
    ]
