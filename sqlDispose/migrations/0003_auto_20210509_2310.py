# Generated by Django 2.2.14 on 2021-05-09 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlDispose', '0002_auto_20210509_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sqldispose',
            name='encoding',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='sqldispose',
            name='ext1',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='sqldispose',
            name='ext2',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='sqldispose',
            name='ext3',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='sqldispose',
            name='ext4',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='sqldispose',
            name='ext5',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='sqldispose',
            name='port',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='sqldispose',
            name='update_person',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
