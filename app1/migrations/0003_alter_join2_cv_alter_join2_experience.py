# Generated by Django 4.0.4 on 2022-05-26 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_join2_rename_message_contactform_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join2',
            name='Cv',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='join2',
            name='Experience',
            field=models.CharField(max_length=30),
        ),
    ]
