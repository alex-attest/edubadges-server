# Generated by Django 3.2.24 on 2024-05-02 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0112_badgeinstance_include_grade_achieved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badgeclass',
            name='assessment_type',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
