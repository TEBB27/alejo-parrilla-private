# Generated by Django 5.0 on 2024-01-01 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=12)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=1000)),
                ('category', models.CharField(choices=[('Carnes', 'Carnes'), ('Pescados', 'Pescados'), ('Típicos', 'Típicos'), ('Bowls', 'Bowls'), ('Menú Infantil', 'Menú Infantil')], max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(blank=True, null=True, upload_to='menu')),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='recomendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='recomendation')),
            ],
        ),
    ]
