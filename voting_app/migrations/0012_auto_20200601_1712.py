# Generated by Django 3.0.6 on 2020-06-01 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0011_transactions_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='event_name',
            field=models.CharField(max_length=150),
        ),
    ]
