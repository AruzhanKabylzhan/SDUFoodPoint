# Generated by Django 4.0.2 on 2022-04-19 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('drink', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('account', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.account')),
                ('drink', models.ManyToManyField(to='drink.Drink')),
                ('food', models.ManyToManyField(to='eat.Eat')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
