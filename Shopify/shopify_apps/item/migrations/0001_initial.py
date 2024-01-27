# Generated by Django 4.2.6 on 2024-01-25 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='item_image')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='item.item')),
                ('processor', models.CharField(blank=True, max_length=32, null=True)),
                ('ram', models.CharField(blank=True, max_length=32, null=True)),
                ('internal_memory', models.CharField(blank=True, max_length=32, null=True)),
                ('GPU', models.CharField(blank=True, max_length=32, null=True)),
            ],
            bases=('item.item',),
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='item.item')),
                ('resolution', models.CharField(blank=True, max_length=128, null=True)),
                ('screen_tech', models.TextField(blank=True, max_length=128, null=True)),
                ('os_version', models.CharField(blank=True, max_length=128, null=True)),
                ('size', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('description', models.TextField(blank=True, max_length=128, null=True)),
            ],
            bases=('item.item',),
        ),
    ]