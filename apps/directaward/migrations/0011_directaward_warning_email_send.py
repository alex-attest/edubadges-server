# Generated by Django 2.2.28 on 2022-11-17 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directaward', '0010_directawardbundle_lti_import'),
    ]

    operations = [
        migrations.AddField(
            model_name='directaward',
            name='warning_email_send',
            field=models.BooleanField(default=False),
        ),
    ]
