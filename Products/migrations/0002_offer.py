# Generated by Django 3.2.20 on 2023-12-27 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('discreption', models.FileField(max_length=255, upload_to='')),
                ('discount', models.FloatField()),
            ],
        ),
    ]
