# Generated by Django 4.2 on 2024-01-28 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='problem',
            new_name='content',
        ),
    ]
