# Generated by Django 4.2.3 on 2023-07-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app11', '0003_person_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='image')),
            ],
        ),
    ]
