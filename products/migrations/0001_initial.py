# Generated by Django 4.0.3 on 2022-05-13 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
                ('about', models.CharField(max_length=1000, verbose_name='О компании')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.CreateModel(
            name='Cotegory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Вид')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('about', models.TextField(verbose_name='О блюде')),
                ('price', models.PositiveIntegerField(null=True, verbose_name='Цена')),
                ('companys', models.ManyToManyField(to='products.company', verbose_name='Изготовитель')),
                ('cotegory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.cotegory')),
            ],
            options={
                'verbose_name': 'Еду',
                'verbose_name_plural': 'Еда',
            },
        ),
    ]
