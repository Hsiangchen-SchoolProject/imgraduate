# Generated by Django 3.0.4 on 2020-05-18 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduateapp', '0002_auto_20200518_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='st_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_number', models.CharField(max_length=8)),
                ('class_number', models.CharField(max_length=8)),
                ('class_name', models.CharField(max_length=20)),
                ('grade', models.IntegerField()),
                ('credit', models.IntegerField()),
                ('term', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='特殊生',
            new_name='special',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='st_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='number',
            new_name='st_number',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='account',
            new_name='st_password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
    ]
