# Generated by Django 3.1.7 on 2021-03-28 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='post',
            table='  tb_posts',
        ),
        migrations.AlterModelTable(
            name='user',
            table='tb_users',
        ),
    ]
