# Generated by Django 5.2 on 2025-04-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_todolist_is_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='is_completed',
            field=models.BooleanField(default=True),
        ),
    ]
