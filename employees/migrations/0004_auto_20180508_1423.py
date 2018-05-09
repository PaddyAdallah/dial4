# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-08 14:23
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employeedetails_emp_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='emp_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]