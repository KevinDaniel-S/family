# Generated by Django 3.2.5 on 2021-07-18 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210718_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='member',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.profile'),
        ),
    ]
