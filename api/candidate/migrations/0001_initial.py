# Generated by Django 4.0.5 on 2022-06-12 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('info_link', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('update', models.DateField(auto_now=True)),
            ],
        ),
    ]
