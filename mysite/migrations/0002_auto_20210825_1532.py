# Generated by Django 3.2.6 on 2021-08-25 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=122),
        ),
    ]
