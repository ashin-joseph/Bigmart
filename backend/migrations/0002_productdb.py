# Generated by Django 5.0.4 on 2024-05-08 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_category', models.CharField(blank=True, max_length=50, null=True)),
                ('p_name', models.CharField(blank=True, max_length=50, null=True)),
                ('p_price', models.IntegerField(blank=True, null=True)),
                ('p_description', models.CharField(blank=True, max_length=100, null=True)),
                ('p_image', models.ImageField(blank=True, null=True, upload_to='prd_pic')),
            ],
        ),
    ]
