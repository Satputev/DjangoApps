# Generated by Django 3.0.4 on 2020-04-05 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app36', '0003_auto_20200405_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='photo',
            field=models.ImageField(upload_to='emp_images/'),
        ),
    ]
