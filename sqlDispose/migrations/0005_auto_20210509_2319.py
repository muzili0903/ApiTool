# Generated by Django 2.2.14 on 2021-05-09 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlDispose', '0004_auto_20210509_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sqldispose',
            name='linkTest',
            field=models.SmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
