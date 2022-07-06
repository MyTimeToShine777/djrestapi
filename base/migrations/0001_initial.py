# Generated by Django 4.0.6 on 2022-07-06 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Batch 2022', max_length=200, verbose_name='Student Name')),
                ('age', models.PositiveIntegerField()),
                ('contact_no', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('qualification', models.CharField(max_length=300, verbose_name='Educational Qulification')),
                ('skills', models.TextField(max_length=1000, verbose_name='IT Skills')),
                ('address', models.TextField(max_length=10000, verbose_name='Native Address')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]