# Generated by Django 3.1.5 on 2021-04-10 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_frd'),
    ]

    operations = [
        migrations.CreateModel(
            name='massage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('whom', models.CharField(max_length=30)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
