# Generated by Django 4.2.6 on 2024-02-05 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='description',
            field=models.TextField(blank=True, max_length=128, null=True),
        ),
    ]
