# Generated by Django 3.2.4 on 2021-07-14 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=25)),
                ('subject', models.CharField(blank=True, max_length=300, null=True)),
                ('day', models.DateField(blank=True, null=True)),
                ('hour', models.DateTimeField(blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
