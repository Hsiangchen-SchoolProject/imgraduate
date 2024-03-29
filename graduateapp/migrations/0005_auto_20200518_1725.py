# Generated by Django 3.0.4 on 2020-05-18 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduateapp', '0004_auto_20200518_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='st_class',
            name='term',
        ),
        migrations.AlterField(
            model_name='st_class',
            name='classify1',
            field=models.CharField(choices=[('必修', '必修'), ('選修', '選修')], default='必修', max_length=10),
        ),
        migrations.AlterField(
            model_name='st_class',
            name='classify2',
            field=models.CharField(choices=[('系上', '系上'), ('通識', '通識')], default='系上', max_length=10),
        ),
        migrations.AlterField(
            model_name='st_class',
            name='credit',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='2', max_length=10),
        ),
        migrations.AlterField(
            model_name='st_class',
            name='grade',
            field=models.IntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='st_class',
            name='year_in_school',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=10),
        ),
    ]
