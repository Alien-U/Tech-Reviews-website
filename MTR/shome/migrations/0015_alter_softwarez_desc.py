# Generated by Django 5.1.5 on 2025-03-06 10:43

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shome', '0014_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softwarez',
            name='desc',
            field=tinymce.models.HTMLField(),
        ),
    ]
