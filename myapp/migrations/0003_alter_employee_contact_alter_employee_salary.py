# Generated by Django 5.1 on 2024-09-22 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_employee_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
