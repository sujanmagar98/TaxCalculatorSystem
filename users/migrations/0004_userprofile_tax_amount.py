# Generated by Django 4.0.3 on 2022-04-09 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='tax_amount',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]