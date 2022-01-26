# Generated by Django 4.0 on 2022-01-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='CustomerCall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(blank=True, help_text='Optional field', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Customer Calls',
            },
        ),
        migrations.CreateModel(
            name='CustomerEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, help_text='Optional field', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Customer Emails',
            },
        ),
    ]
