# Generated by Django 5.0.3 on 2024-03-27 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitalapp', '0008_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=250)),
                ('place', models.CharField(max_length=100)),
            ],
        ),
    ]