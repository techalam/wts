# Generated by Django 4.0.4 on 2022-05-26 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_join2_cv_alter_join2_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join2',
            name='Remote',
        ),
    ]
