# Generated by Django 5.0.3 on 2024-03-27 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='branch')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Enquery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('number', models.IntegerField(unique=True)),
                ('message', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='gallerys')),
            ],
            options={
                'ordering': ('image',),
            },
        ),
        migrations.CreateModel(
            name='Homes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='homes')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='package')),
                ('price', models.IntegerField()),
                ('ln1', models.CharField(max_length=400)),
                ('ln2', models.CharField(max_length=400)),
                ('ln3', models.CharField(max_length=400)),
                ('ln4', models.CharField(max_length=400)),
                ('ln5', models.CharField(max_length=400)),
                ('ln6', models.CharField(max_length=400)),
                ('ln7', models.CharField(blank=True, max_length=400)),
                ('ln8', models.CharField(blank=True, max_length=400)),
                ('ln9', models.CharField(blank=True, max_length=400)),
                ('ln10', models.CharField(blank=True, max_length=400)),
                ('ln11', models.CharField(blank=True, max_length=400)),
                ('ln12', models.CharField(blank=True, max_length=400)),
                ('ln13', models.CharField(blank=True, max_length=400)),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]