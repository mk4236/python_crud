# Generated by Django 3.2.5 on 2022-03-11 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='최종수정일'),
        ),
        migrations.AlterField(
            model_name='user',
            name='insert_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='등록일'),
        ),
    ]