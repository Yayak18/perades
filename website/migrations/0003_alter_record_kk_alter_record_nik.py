# Generated by Django 5.1 on 2024-08-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_record_hp_alter_record_kk_alter_record_nik_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='KK',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='NIK',
            field=models.BigIntegerField(),
        ),
    ]
