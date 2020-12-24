# Generated by Django 3.0.4 on 2020-03-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoachingCenterRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('addr', models.CharField(max_length=150)),
                ('coaching_provided', models.CharField(max_length=20)),
                ('cno', models.IntegerField()),
                ('iId', models.CharField(max_length=30, unique=True)),
                ('established', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='LoginDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=15)),
                ('Uname', models.CharField(max_length=30, unique=True)),
                ('Upwd', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Age', models.IntegerField()),
                ('Contact', models.IntegerField()),
                ('Address', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=10)),
                ('Sport', models.CharField(max_length=15)),
                ('Ptype', models.CharField(max_length=10)),
                ('Uname', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]
