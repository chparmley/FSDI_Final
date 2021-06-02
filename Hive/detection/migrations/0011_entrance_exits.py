# Generated by Django 3.2.2 on 2021-05-20 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0010_auto_20210520_0444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeIn', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeOut', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]