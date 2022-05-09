# Generated by Django 4.0.3 on 2022-05-09 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=30, null=True)),
                ('lname', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.TextField(max_length=900, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]
