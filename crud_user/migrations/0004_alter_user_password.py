# Generated by Django 4.1.5 on 2023-01-11 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_user', '0003_rename_addres_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
