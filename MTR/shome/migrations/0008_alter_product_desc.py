# Generated by Django 5.1.5 on 2025-03-01 04:17

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shome', '0007_alter_gaming_desc_alter_product_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=tinymce.models.HTMLField(),
        ),
    ]
