# Generated by Django 3.0.4 on 2020-04-10 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BranchesModel',
            fields=[
                ('branch_name', models.CharField(max_length=30)),
                ('b_code', models.IntegerField(primary_key=True, serialize=False)),
                ('b_address', models.TextField()),
                ('b_contact', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OwnersModel',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('contactno', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=10)),
                ('status', models.BooleanField()),
                ('photo', models.ImageField(upload_to='owners_images/')),
            ],
        ),
        migrations.CreateModel(
            name='CustomersModel',
            fields=[
                ('cust_name', models.CharField(max_length=30)),
                ('cust_contact', models.IntegerField(primary_key=True, serialize=False)),
                ('cust_addr', models.TextField()),
                ('cust_image', models.ImageField(upload_to='cust_images/')),
                ('br_name', models.ManyToManyField(to='app41.BranchesModel')),
            ],
        ),
        migrations.CreateModel(
            name='CompaniesModel',
            fields=[
                ('c_name', models.CharField(max_length=30)),
                ('ISONO', models.IntegerField(primary_key=True, serialize=False)),
                ('mainBranch_addr', models.TextField()),
                ('c_contact', models.IntegerField(unique=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app41.OwnersModel')),
            ],
        ),
        migrations.AddField(
            model_name='branchesmodel',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app41.CompaniesModel'),
        ),
    ]
