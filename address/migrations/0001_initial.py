# Generated by Django 2.2.5 on 2019-09-05 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.TextField()),
                ('building_number', models.CharField(max_length=10)),
                ('postal_code', models.CharField(max_length=15)),
                ('locality', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'company_address',
            },
        ),
    ]
