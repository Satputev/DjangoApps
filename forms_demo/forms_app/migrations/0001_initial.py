# Generated by Django 3.0.4 on 2020-04-08 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField(unique=True)),
                ('ename', models.CharField(max_length=30)),
                ('contact_no', models.IntegerField()),
                ('salary', models.FloatField()),
                ('Designation', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
