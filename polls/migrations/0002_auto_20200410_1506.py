# Generated by Django 2.2.1 on 2020-04-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.CharField(max_length=200),
        ),
    ]
