# Generated by Django 5.1.7 on 2025-05-10 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_product_specification_specification_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specification',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='specifications',
            field=models.ManyToManyField(blank=True, to='main.specification'),
        ),
    ]
