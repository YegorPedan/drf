# Generated by Django 4.2.6 on 2023-10-16 14:07

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
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('pub_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField(blank=True, null=True)),
                ('biography', models.TextField()),
                ('books', models.ManyToManyField(related_name='authors', to='main.book')),
            ],
        ),
    ]