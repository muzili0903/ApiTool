# Generated by Django 2.2.14 on 2021-05-10 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlDispose', '0006_auto_20210510_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sqldispose',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
