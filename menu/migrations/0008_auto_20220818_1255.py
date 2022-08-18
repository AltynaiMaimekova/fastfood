# Generated by Django 3.2 on 2022-08-18 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_auto_20220818_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='menu.user'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='menu.user'),
        ),
    ]
