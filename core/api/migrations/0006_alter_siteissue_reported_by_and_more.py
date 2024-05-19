# Generated by Django 5.0.6 on 2024-05-19 21:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_siteissue_supporting_document'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteissue',
            name='reported_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='siteissue',
            name='supporting_document',
            field=models.FileField(default=1, upload_to='supporting_documents/'),
            preserve_default=False,
        ),
    ]