# Generated by Django 5.1.5 on 2025-03-06 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shome', '0012_delete_blogcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('message', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
