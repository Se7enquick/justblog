# Generated by Django 3.2.9 on 2021-11-15 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_child',
            field=models.BooleanField(default=False),
        ),
    ]
