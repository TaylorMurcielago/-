# Generated by Django 2.2.4 on 2019-08-27 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190827_1032'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='grade',
            field=models.IntegerField(null=True, verbose_name='年级'),
        ),
    ]