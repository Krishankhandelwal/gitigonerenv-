# Generated by Django 5.0.7 on 2024-07-18 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
