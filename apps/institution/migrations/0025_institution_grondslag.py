# Generated by Django 2.2.13 on 2020-07-29 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0025_auto_20200723_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='grondslag',
            field=models.CharField(choices=[('uitvoering_overeenkomst', 'uitvoering_overeenkomst'), ('gerechtvaardigd_belang', 'gerechtvaardigd_belang'), ('wettelijke_verplichting', 'wettelijke_verplichting')], default='uitvoering_overeenkomst', max_length=254),
        ),
    ]
