# Generated by Django 2.2.14 on 2021-05-09 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlDispose', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sqldispose',
            name='linkTest',
            field=models.SmallIntegerField(default=0),
        ),
    ]