# Generated by Django 4.0.3 on 2022-04-16 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_tax_info_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tax_info',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]