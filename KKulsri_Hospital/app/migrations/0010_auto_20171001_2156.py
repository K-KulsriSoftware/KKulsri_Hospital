# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-01 14:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20171001_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Religion',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Status',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='blood_group_abo',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='blood_group_rh',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='congenital_disease',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='emergency_addr',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='emergency_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='emergency_phone',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='id_card_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='mother_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='nationallity',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='occupy',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pateint_address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='patient_img',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='patient_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='patient_name_title',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='patient_surname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='race',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='telphone_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]