# Generated by Django 2.0.3 on 2018-03-21 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apfifogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='name_of_fs',
            new_name='name_of_fachschaft',
        ),
    ]