# Generated by Django 4.0.2 on 2022-02-16 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='text',
        ),
    ]
