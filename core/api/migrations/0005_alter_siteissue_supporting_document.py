# Generated by Django 5.0.6 on 2024-05-19 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_siteissue_supporting_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteissue',
            name='supporting_document',
            field=models.FileField(blank=True, null=True, upload_to='supporting_documents/'),
        ),
    ]
