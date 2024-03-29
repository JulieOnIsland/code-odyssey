# Generated by Django 5.0.1 on 2024-02-05 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=20)),
                ('link', models.TextField()),
                ('num', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('timeLimits', models.CharField(max_length=200)),
                ('memoryLimits', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('inputSample', models.TextField(blank=True, null=True)),
                ('outputSample', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.TextField()),
                ('no', models.IntegerField()),
                ('code', models.TextField()),
                ('time', models.TextField()),
                ('memory', models.TextField()),
            ],
        ),
    ]
