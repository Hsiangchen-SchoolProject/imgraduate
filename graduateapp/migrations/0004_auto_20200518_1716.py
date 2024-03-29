# Generated by Django 3.0.4 on 2020-05-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduateapp', '0003_auto_20200518_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='st_class',
            name='classify1',
            field=models.CharField(choices=[('必修', '必修'), ('選修', '選修')], default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='st_class',
            name='classify2',
            field=models.CharField(choices=[('系上', '系上'), ('通識', '通識')], default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='st_class',
            name='year_in_school',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='st_class',
            name='grade',
            field=models.IntegerField(default=None),
        ),
    ]
