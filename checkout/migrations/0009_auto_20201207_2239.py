# Generated by Django 3.0.1 on 2020-12-07 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_auto_20201207_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(editable=False, verbose_name='Date of order'),
        ),
    ]
