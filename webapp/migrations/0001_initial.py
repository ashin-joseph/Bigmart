# Generated by Django 5.0.4 on 2024-05-11 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=50, null=True)),
                ('contact_number', models.IntegerField(blank=True, null=True)),
                ('contact_subject', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_message', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
