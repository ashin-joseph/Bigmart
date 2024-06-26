# Generated by Django 5.0.4 on 2024-06-10 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_cartdb_delete_reg_signin'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkoutDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_username', models.CharField(blank=True, max_length=50, null=True)),
                ('checkout_email', models.EmailField(blank=True, max_length=50, null=True)),
                ('checkout_place', models.CharField(blank=True, max_length=50, null=True)),
                ('checkout_address', models.TextField(blank=True, null=True)),
                ('checkout_Phone', models.IntegerField(blank=True, null=True)),
                ('checkout_message', models.TextField(blank=True, null=True)),
                ('checkout_overall_total', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
