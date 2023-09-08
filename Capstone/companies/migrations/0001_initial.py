# Generated by Django 4.2.4 on 2023-09-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2048)),
                ('image', models.ImageField(upload_to='images/')),
                ('field', models.CharField(max_length=2048)),
                ('info', models.TextField()),
                ('description', models.TextField()),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]