# Generated by Django 5.1.7 on 2025-03-15 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=225)),
                ('publication_year', models.IntegerField()),
                ('publisher', models.CharField(blank=True, max_length=225, null=True)),
                ('edition', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
