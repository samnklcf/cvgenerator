# Generated by Django 3.2.6 on 2021-12-20 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='experience',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
