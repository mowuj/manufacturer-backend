# Generated by Django 4.2 on 2024-01-31 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='tool.category'),
        ),
    ]
