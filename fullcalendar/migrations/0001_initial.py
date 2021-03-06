# Generated by Django 3.0.1 on 2020-08-14 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name=['%Y-%m-%d %H:%M:%S'])),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name=['%Y-%m-%d %H:%M:%S'])),
            ],
        ),
    ]
