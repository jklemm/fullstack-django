# Generated by Django 3.2.7 on 2021-09-13 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210913_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='updated_at',
            field=models.DateField(null=True),
        ),
    ]
