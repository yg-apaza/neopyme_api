# Generated by Django 3.1.1 on 2020-10-17 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_sources', '0002_financialproduct_petitioner_purpose_requestedfinantialproduct_requirement'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialproduct',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
