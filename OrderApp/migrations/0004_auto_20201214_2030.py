# Generated by Django 3.1.3 on 2020-12-15 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderApp', '0003_auto_20201214_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditemsmodel',
            name='table_id',
            field=models.CharField(default='1', max_length=10, null=True),
        ),
    ]