# Generated by Django 3.2.5 on 2021-07-20 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_membership_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='family',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='member',
        ),
        migrations.DeleteModel(
            name='Family',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
    ]
