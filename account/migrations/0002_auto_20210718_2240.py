# Generated by Django 3.2.5 on 2021-07-18 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command_level', models.IntegerField(choices=[(0, 'Member'), (2, 'Head Household')])),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.family')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile', unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='family',
            name='members',
            field=models.ManyToManyField(through='account.Membership', to='account.Profile'),
        ),
    ]
