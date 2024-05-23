# Generated by Django 5.0.6 on 2024-05-23 07:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_district_province'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.province'),
            preserve_default=False,
        ),
    ]
